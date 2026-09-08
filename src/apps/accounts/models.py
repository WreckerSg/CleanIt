from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Usuario de CleanIt con una responsabilidad funcional explícita."""

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        PARTICIPANT = "PARTICIPANT", "Participante"

    email = models.EmailField("correo electrónico", unique=True)
    role = models.CharField(
        "rol",
        max_length=20,
        choices=Role.choices,
        default=Role.PARTICIPANT,
    )

    REQUIRED_FIELDS = ["email"]

    @property
    def is_administrator(self) -> bool:
        return self.role == self.Role.ADMIN or self.is_superuser

    def __str__(self) -> str:
        return self.get_full_name() or self.username
