from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ChoreForm, ZoneForm
from .models import Chore, Zone
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
