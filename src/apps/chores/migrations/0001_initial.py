# Generated for CleanIt with Django 5.2.17.

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Zone",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80, unique=True, verbose_name="nombre")),
                ("description", models.TextField(blank=True, verbose_name="descripción")),
                ("is_active", models.BooleanField(default=True, verbose_name="activa")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="última actualización")),
            ],
            options={
                "verbose_name": "zona",
                "verbose_name_plural": "zonas",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Chore",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="nombre")),
                ("description", models.TextField(blank=True, verbose_name="descripción")),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("ONCE", "Única"),
                            ("DAILY", "Diaria"),
                            ("WEEKLY", "Semanal"),
                            ("MONTHLY", "Mensual"),
                        ],
                        default="ONCE",
                        max_length=12,
                        verbose_name="frecuencia",
                    ),
                ),
                ("next_due_date", models.DateField(verbose_name="próxima fecha")),
                ("is_active", models.BooleanField(default=True, verbose_name="activa")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="última actualización")),
                (
                    "assignee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="assigned_chores",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="responsable",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created_chores",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="creada por",
                    ),
                ),
                (
                    "zone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="chores",
                        to="chores.zone",
                        verbose_name="zona",
                    ),
                ),
            ],
            options={
                "verbose_name": "tarea",
                "verbose_name_plural": "tareas",
                "ordering": ("-is_active", "next_due_date", "name"),
            },
        ),
    ]
