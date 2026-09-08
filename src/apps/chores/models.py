from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


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

    def __str__(self) -> str:
        return f"{self.name} - {self.zone}"
