from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User


class DashboardTests(TestCase):
    def test_dashboard_requires_authentication(self):
        response = self.client.get(reverse("dashboard"))

        self.assertRedirects(response, f'{reverse("login")}?next=/')

    def test_participant_sees_personal_options(self):
        user = User.objects.create_user(
            username="participante",
            email="participante@example.com",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("dashboard"))

        self.assertContains(response, "Mis tareas pendientes")
        self.assertNotContains(response, "Administrar usuarios")

    def test_administrator_sees_management_option(self):
        user = User.objects.create_user(
            username="administrador",
            email="administrador@example.com",
            role=User.Role.ADMIN,
        )
        self.client.force_login(user)

        response = self.client.get(reverse("dashboard"))

        self.assertContains(response, "Administrar usuarios")
