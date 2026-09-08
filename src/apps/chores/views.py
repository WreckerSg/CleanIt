from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.db.models import Exists, OuterRef, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.dateparse import parse_date

from .forms import ChoreForm, CompletionForm, ZoneForm
from .models import Chore, Completion, Zone
from .permissions import administrator_required


@administrator_required
def zone_list(request):
    return render(request, "chores/zone_list.html", {"zones": Zone.objects.all()})


@administrator_required
def zone_create(request):
    form = ZoneForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "La zona fue creada correctamente.")
        return redirect("zone_list")
    return render(
        request,
        "chores/form.html",
        {"form": form, "title": "Nueva zona", "cancel_url": "zone_list"},
    )


@administrator_required
def zone_edit(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    form = ZoneForm(request.POST or None, instance=zone)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "La zona fue actualizada correctamente.")
        return redirect("zone_list")
    return render(
        request,
        "chores/form.html",
        {"form": form, "title": "Editar zona", "cancel_url": "zone_list"},
    )


@administrator_required
def zone_deactivate(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    if request.method == "POST":
        if zone.chores.filter(is_active=True).exists():
            messages.error(
                request,
                "No se puede desactivar una zona que contiene tareas activas.",
            )
        else:
            zone.is_active = False
            zone.save(update_fields=["is_active", "updated_at"])
            messages.success(request, "La zona fue desactivada.")
    return redirect("zone_list")


@administrator_required
def chore_list(request):
    chores = Chore.objects.select_related("zone", "assignee")
    return render(request, "chores/chore_list.html", {"chores": chores})


@administrator_required
def chore_create(request):
    form = ChoreForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        chore = form.save(commit=False)
        chore.created_by = request.user
        chore.save()
        messages.success(request, "La tarea fue creada correctamente.")
        return redirect("chore_list")
    return render(
        request,
        "chores/form.html",
        {"form": form, "title": "Nueva tarea", "cancel_url": "chore_list"},
    )


@administrator_required
def chore_edit(request, pk):
    chore = get_object_or_404(Chore, pk=pk)
    form = ChoreForm(request.POST or None, instance=chore)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "La tarea fue actualizada correctamente.")
        return redirect("chore_list")
    return render(
        request,
        "chores/form.html",
        {"form": form, "title": "Editar tarea", "cancel_url": "chore_list"},
    )


@administrator_required
def chore_retire(request, pk):
    chore = get_object_or_404(Chore, pk=pk)
    if request.method == "POST":
        chore.is_active = False
        chore.save(update_fields=["is_active", "updated_at"])
        messages.success(request, "La tarea fue retirada y conservará su historial.")
    return redirect("chore_list")


@login_required
def pending_chore_list(request):
    """Muestra las tareas activas asignadas al usuario autenticado."""

    once_completed = Exists(Completion.objects.filter(chore=OuterRef("pk")))
    recurring = (
        Chore.Frequency.DAILY,
        Chore.Frequency.WEEKLY,
        Chore.Frequency.MONTHLY,
    )
    chores = (
        Chore.objects.select_related("zone")
        .annotate(once_completed=once_completed)
        .filter(is_active=True, assignee=request.user)
        .filter(Q(frequency__in=recurring) | Q(once_completed=False))
    )
    zones = Zone.objects.filter(
        chores__assignee=request.user,
        chores__is_active=True,
    ).distinct()
    selected_zone = request.GET.get("zone", "")
    selected_status = request.GET.get("status", "all")
    if selected_zone.isdigit():
        chores = chores.filter(zone_id=int(selected_zone))
    if selected_status == "overdue":
        chores = chores.filter(next_due_date__lt=timezone.localdate())
    elif selected_status == "pending":
        chores = chores.filter(next_due_date__gte=timezone.localdate())
    return render(
        request,
        "chores/pending_list.html",
        {
            "chores": chores,
            "zones": zones,
            "selected_zone": selected_zone,
            "selected_status": selected_status,
        },
    )


@login_required
def chore_complete(request, pk):
    chore = get_object_or_404(
        Chore.objects.select_related("zone"),
        pk=pk,
        assignee=request.user,
        is_active=True,
    )
    if chore.frequency == Chore.Frequency.ONCE and chore.completions.exists():
        messages.info(request, "Esta tarea única ya fue completada.")
        return redirect("pending_chore_list")

    form = CompletionForm(
        request.POST or None,
        initial={"scheduled_for": chore.next_due_date},
    )
    if request.method == "POST" and form.is_valid():
        try:
            with transaction.atomic():
                locked_chore = Chore.objects.select_for_update().get(pk=chore.pk)
                if (
                    not locked_chore.is_active
                    or locked_chore.assignee_id != request.user.pk
                ):
                    messages.error(
                        request, "La tarea ya no está disponible para completar."
                    )
                    return redirect("pending_chore_list")
                scheduled_for = form.cleaned_data["scheduled_for"]
                if scheduled_for != locked_chore.next_due_date:
                    messages.info(
                        request,
                        "Esta ocurrencia ya fue registrada o cambió de fecha.",
                    )
                    return redirect("pending_chore_list")
                if (
                    locked_chore.frequency == Chore.Frequency.ONCE
                    and locked_chore.completions.exists()
                ):
                    messages.info(request, "Esta tarea única ya fue completada.")
                    return redirect("pending_chore_list")
                completion = form.save(commit=False)
                completion.chore = locked_chore
                completion.completed_by = request.user
                completion.completed_at = timezone.now()
                completion.scheduled_for = scheduled_for
                completion.full_clean()
                completion.save()
                locked_chore.advance_after_completion(timezone.localdate())
                locked_chore.save(
                    update_fields=[
                        "next_due_date",
                        "recurrence_anchor_day",
                        "updated_at",
                    ]
                )
        except IntegrityError:
            messages.info(request, "Esta ocurrencia ya fue registrada.")
            return redirect("pending_chore_list")
        messages.success(request, "El cumplimiento fue registrado correctamente.")
        return redirect("pending_chore_list")

    return render(
        request,
        "chores/complete.html",
        {"form": form, "chore": chore},
    )


@login_required
def history_list(request):
    completions = Completion.objects.select_related(
        "chore", "chore__zone", "completed_by"
    )
    if not request.user.is_administrator:
        completions = completions.filter(completed_by=request.user)
    available_completions = completions
    selected_zone = request.GET.get("zone", "")
    selected_user = request.GET.get("user", "")
    date_from_value = request.GET.get("date_from", "")
    date_to_value = request.GET.get("date_to", "")
    if selected_zone.isdigit():
        completions = completions.filter(chore__zone_id=int(selected_zone))
    if request.user.is_administrator and selected_user.isdigit():
        completions = completions.filter(completed_by_id=int(selected_user))
    date_from = parse_date(date_from_value)
    date_to = parse_date(date_to_value)
    if date_from:
        completions = completions.filter(completed_at__date__gte=date_from)
    if date_to:
        completions = completions.filter(completed_at__date__lte=date_to)

    zones = Zone.objects.filter(
        pk__in=available_completions.values_list("chore__zone_id", flat=True)
    ).distinct()
    users = get_user_model().objects.none()
    if request.user.is_administrator:
        users = get_user_model().objects.filter(
            pk__in=available_completions.values_list("completed_by_id", flat=True)
        ).distinct()
    return render(
        request,
        "chores/history_list.html",
        {
            "completions": completions,
            "zones": zones,
            "users": users,
            "selected_zone": selected_zone,
            "selected_user": selected_user,
            "date_from": date_from_value,
            "date_to": date_to_value,
        },
    )
