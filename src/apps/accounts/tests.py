import secrets

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

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

    def test_valid_credentials_create_a_session(self):
        test_password = secrets.token_urlsafe(18)
        user = User.objects.create_user(
            username="participante",
            email="participante@example.com",
            password=test_password,
        )

        response = self.client.post(
            reverse("login"),
            {"username": user.username, "password": test_password},
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_invalid_credentials_show_a_generic_message(self):
        test_password = secrets.token_urlsafe(18)
        User.objects.create_user(
            username="participante",
            email="participante@example.com",
            password=test_password,
        )

        response = self.client.post(
            reverse("login"),
            {"username": "participante", "password": secrets.token_urlsafe(18)},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "El usuario o la contraseña no son correctos.")
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_duplicate_email_is_rejected(self):
        User.objects.create_user(username="ana", email="persona@example.com")
        duplicate = User(username="maria", email="persona@example.com")

        with self.assertRaises(ValidationError):
            duplicate.full_clean()

    def test_user_edit_and_deactivation_preserve_identity(self):
        user = User.objects.create_user(username="ana", email="ana@example.com")
        original_pk = user.pk

        user.first_name = "Ana María"
        user.is_active = False
        user.save()
        user.refresh_from_db()

        self.assertEqual(user.pk, original_pk)
        self.assertEqual(user.first_name, "Ana María")
        self.assertFalse(user.is_active)
