from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User

from .forms import ChoreForm
from .models import Chore, Zone


class ChoreManagementTests(TestCase):
    def setUp(self):
        self.administrator = User.objects.create_user(
            username="coordinador",
            email="coordinador@example.com",
            role=User.Role.ADMIN,
        )
        self.participant = User.objects.create_user(
            username="participante",
            email="participante@example.com",
        )
        self.zone = Zone.objects.create(name="Cocina")

    def create_chore(self, **changes):
        values = {
            "name": "Trapear el piso",
            "zone": self.zone,
            "assignee": self.participant,
            "frequency": Chore.Frequency.WEEKLY,
            "next_due_date": date(2026, 9, 15),
            "created_by": self.administrator,
        }
        values.update(changes)
        return Chore.objects.create(**values)

    def test_inactive_zone_is_rejected_by_model(self):
        self.zone.is_active = False
        self.zone.save()
        chore = Chore(
            name="Limpiar mesa",
            zone=self.zone,
            assignee=self.participant,
            next_due_date=date(2026, 9, 15),
        )

        with self.assertRaises(ValidationError):
            chore.full_clean()

    def test_inactive_assignee_is_rejected_by_form(self):
        self.participant.is_active = False
        self.participant.save()
        form = ChoreForm(
            data={
                "name": "Limpiar mesa",
                "description": "",
                "zone": self.zone.pk,
                "assignee": self.participant.pk,
                "frequency": Chore.Frequency.ONCE,
                "next_due_date": "2026-09-15",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("assignee", form.errors)

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse("chore_list"))

        self.assertRedirects(response, f'{reverse("login")}?next=/gestion/tareas/')

    def test_participant_cannot_open_management(self):
        self.client.force_login(self.participant)

        response = self.client.get(reverse("chore_list"))

        self.assertEqual(response.status_code, 403)

    def test_administrator_can_create_zone(self):
        self.client.force_login(self.administrator)

        response = self.client.post(
            reverse("zone_create"),
            {"name": "Baño", "description": "Baño principal"},
        )

        self.assertRedirects(response, reverse("zone_list"))
        self.assertTrue(Zone.objects.filter(name="Baño", is_active=True).exists())

    def test_administrator_pages_render(self):
        self.client.force_login(self.administrator)

        for route_name in ("zone_list", "zone_create", "chore_list", "chore_create"):
            with self.subTest(route=route_name):
                response = self.client.get(reverse(route_name))
                self.assertEqual(response.status_code, 200)

    def test_administrator_can_create_chore(self):
        self.client.force_login(self.administrator)

        response = self.client.post(
            reverse("chore_create"),
            {
                "name": "Sacar la basura",
                "description": "Llevar las bolsas al punto de recolección",
                "zone": self.zone.pk,
                "assignee": self.participant.pk,
                "frequency": Chore.Frequency.DAILY,
                "next_due_date": "2026-09-15",
            },
        )

        self.assertRedirects(response, reverse("chore_list"))
        chore = Chore.objects.get(name="Sacar la basura")
        self.assertEqual(chore.created_by, self.administrator)
        self.assertEqual(chore.assignee, self.participant)

    def test_chore_is_retired_only_by_post(self):
        chore = self.create_chore()
        self.client.force_login(self.administrator)

        self.client.get(reverse("chore_retire", args=[chore.pk]))
        chore.refresh_from_db()
        self.assertTrue(chore.is_active)

        self.client.post(reverse("chore_retire", args=[chore.pk]))
        chore.refresh_from_db()
        self.assertFalse(chore.is_active)

    def test_zone_with_active_chore_cannot_be_deactivated(self):
        self.create_chore()
        self.client.force_login(self.administrator)

        self.client.post(reverse("zone_deactivate", args=[self.zone.pk]))

        self.zone.refresh_from_db()
        self.assertTrue(self.zone.is_active)

    def test_participant_cannot_create_zone_by_direct_post(self):
        self.client.force_login(self.participant)

        response = self.client.post(reverse("zone_create"), {"name": "Sala"})

        self.assertEqual(response.status_code, 403)
        self.assertFalse(Zone.objects.filter(name="Sala").exists())
