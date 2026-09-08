import calendar
from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Zone(models.Model):
    name = models.CharField("nombre", max_length=80, unique=True)
    description = models.TextField("descripción", blank=True)
    is_active = models.BooleanField("activa", default=True)
    created_at = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("última actualización", auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "zona"
        verbose_name_plural = "zonas"

    def __str__(self) -> str:
        return self.name


class Chore(models.Model):
    class Frequency(models.TextChoices):
        ONCE = "ONCE", "Única"
        DAILY = "DAILY", "Diaria"
        WEEKLY = "WEEKLY", "Semanal"
        MONTHLY = "MONTHLY", "Mensual"

    name = models.CharField("nombre", max_length=120)
    description = models.TextField("descripción", blank=True)
    zone = models.ForeignKey(
        Zone,
        on_delete=models.PROTECT,
        related_name="chores",
        verbose_name="zona",
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="assigned_chores",
        verbose_name="responsable",
    )
    frequency = models.CharField(
        "frecuencia",
        max_length=12,
        choices=Frequency.choices,
        default=Frequency.ONCE,
    )
    recurrence_anchor_day = models.PositiveSmallIntegerField(
        "día ancla de recurrencia",
        null=True,
        blank=True,
        editable=False,
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    next_due_date = models.DateField("próxima fecha")
    is_active = models.BooleanField("activa", default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_chores",
        verbose_name="creada por",
    )
    created_at = models.DateTimeField("fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("última actualización", auto_now=True)

    class Meta:
        ordering = ("-is_active", "next_due_date", "name")
        verbose_name = "tarea"
        verbose_name_plural = "tareas"

    def clean(self):
        errors = {}
        if self.zone_id and not self.zone.is_active:
            errors["zone"] = "No se puede asignar una tarea a una zona inactiva."
        if self.assignee_id and not self.assignee.is_active:
            errors["assignee"] = "No se puede asignar una tarea a una persona inactiva."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        if self.next_due_date and self.recurrence_anchor_day is None:
            self.recurrence_anchor_day = self.next_due_date.day
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.zone}"

    @property
    def status_label(self) -> str:
        """Etiqueta administrativa que distingue retiro de cumplimiento."""

        if not self.is_active:
            return "Retirada"
        if self.frequency == self.Frequency.ONCE and self.completions.exists():
            return "Completada"
        return "Activa"

    @property
    def is_overdue(self) -> bool:
        return self.is_active and self.next_due_date < timezone.localdate()

    def advance_after_completion(self, completed_on=None):
        """Actualiza la próxima fecha de una tarea recurrente."""

        if self.frequency == self.Frequency.ONCE:
            return

        completed_on = completed_on or timezone.localdate()
        next_date = self.next_due_date
        while next_date <= completed_on:
            if self.frequency == self.Frequency.DAILY:
                next_date = next_date + timedelta(days=1)
            elif self.frequency == self.Frequency.WEEKLY:
                next_date = next_date + timedelta(days=7)
            else:
                month = next_date.month + 1
                year = next_date.year
                if month > 12:
                    month = 1
                    year += 1
                anchor_day = self.recurrence_anchor_day or next_date.day
                day = min(anchor_day, calendar.monthrange(year, month)[1])
                next_date = next_date.replace(year=year, month=month, day=day)
        self.next_due_date = next_date


class Completion(models.Model):
    chore = models.ForeignKey(
        Chore,
        on_delete=models.PROTECT,
        related_name="completions",
        verbose_name="tarea",
    )
    completed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="chore_completions",
        verbose_name="realizada por",
    )
    note = models.TextField("observación", blank=True)
    scheduled_for = models.DateField(
        "fecha programada",
        default=timezone.localdate,
    )
    completed_at = models.DateTimeField(
        "fecha de cumplimiento",
        default=timezone.now,
        editable=False,
    )

    class Meta:
        ordering = ("-completed_at",)
        verbose_name = "cumplimiento"
        verbose_name_plural = "cumplimientos"
        constraints = [
            models.UniqueConstraint(
                fields=("chore", "scheduled_for"),
                name="one_completion_per_occurrence",
            )
        ]

    def clean(self):
        if (
            self.chore_id
            and self.completed_by_id
            and self.completed_by_id != self.chore.assignee_id
        ):
            raise ValidationError(
                {"completed_by": "Solo la persona asignada puede registrar el cumplimiento."}
            )

    def __str__(self) -> str:
        return f"{self.chore.name} - {self.completed_by}"
