import secrets

from django.contrib.auth import authenticate
from django.test import TestCase

from .models import User


class UserModelTests(TestCase):
    def test_new_user_is_participant_by_default(self):
        user = User.objects.create_user(
            username="ana",
            email="ana@example.com",
        )

        self.assertEqual(user.role, User.Role.PARTICIPANT)
        self.assertFalse(user.is_administrator)

    def test_admin_role_is_recognized(self):
        user = User.objects.create_user(
            username="coordinador",
            email="coordinador@example.com",
            role=User.Role.ADMIN,
        )

        self.assertTrue(user.is_administrator)

    def test_superuser_receives_admin_role(self):
        user = User.objects.create_superuser(
            username="superusuario",
            email="superusuario@example.com",
        )

        self.assertEqual(user.role, User.Role.ADMIN)
        self.assertEqual(user.role_name, "Administrador")

    def test_inactive_user_cannot_authenticate(self):
        test_password = secrets.token_urlsafe(18)
        User.objects.create_user(
            username="inactivo",
            email="inactivo@example.com",
            password=test_password,
            is_active=False,
        )

        user = authenticate(username="inactivo", password=test_password)

        self.assertIsNone(user)
