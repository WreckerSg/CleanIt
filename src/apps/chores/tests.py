from datetime import date
from unittest.mock import patch

from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from apps.accounts.models import User

from .forms import ChoreForm
from .models import Chore, Completion, Zone


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

    def test_participant_sees_only_assigned_active_chores(self):
        assigned = self.create_chore(name="Limpiar cocina")
        other_user = User.objects.create_user(
            username="otra", email="otra@example.com"
        )
        self.create_chore(name="Limpiar patio", assignee=other_user)
        self.create_chore(name="Limpiar ventana", is_active=False)
        self.client.force_login(self.participant)

        response = self.client.get(reverse("pending_chore_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, assigned.name)
        self.assertNotContains(response, "Limpiar patio")
        self.assertNotContains(response, "Limpiar ventana")

    def test_anonymous_user_is_redirected_from_pending(self):
        response = self.client.get(reverse("pending_chore_list"))

        self.assertRedirects(
            response,
            f'{reverse("login")}?next=/gestion/tareas/pendientes/',
        )

    def test_participant_can_open_completion_form(self):
        chore = self.create_chore()
        self.client.force_login(self.participant)

        response = self.client.get(reverse("chore_complete", args=[chore.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registrar cumplimiento")
        self.assertContains(response, chore.name)
        self.assertFalse(Completion.objects.exists())

    def test_one_time_completion_is_recorded_and_removed_from_pending(self):
        chore = self.create_chore(frequency=Chore.Frequency.ONCE)
        self.client.force_login(self.participant)

        response = self.client.post(
            reverse("chore_complete", args=[chore.pk]),
            {
                "note": "Se limpió completamente.",
                "scheduled_for": "2026-09-15",
            },
        )

        self.assertRedirects(response, reverse("pending_chore_list"))
        completion = Completion.objects.get(chore=chore)
        self.assertEqual(completion.completed_by, self.participant)
        self.assertEqual(completion.note, "Se limpió completamente.")
        pending = self.client.get(reverse("pending_chore_list"))
        self.assertNotContains(pending, chore.name)

    def test_recurring_completion_advances_next_due_date(self):
        chore = self.create_chore(
            frequency=Chore.Frequency.WEEKLY,
            next_due_date=date(2026, 9, 1),
        )
        self.client.force_login(self.participant)

        with patch(
            "apps.chores.views.timezone.localdate",
            return_value=date(2026, 9, 8),
        ):
            response = self.client.post(
                reverse("chore_complete", args=[chore.pk]),
                {"note": "Listo", "scheduled_for": "2026-09-01"},
            )

        self.assertRedirects(response, reverse("pending_chore_list"))
        chore.refresh_from_db()
        self.assertEqual(chore.next_due_date, date(2026, 9, 15))
        self.assertTrue(Completion.objects.filter(chore=chore).exists())

    def test_participant_cannot_complete_another_users_chore(self):
        other_user = User.objects.create_user(
            username="otra", email="otra@example.com"
        )
        chore = self.create_chore(assignee=other_user)
        self.client.force_login(self.participant)

        response = self.client.get(reverse("chore_complete", args=[chore.pk]))

        self.assertEqual(response.status_code, 404)

    def test_history_is_filtered_for_participants(self):
        own_chore = self.create_chore(name="Propia")
        other_user = User.objects.create_user(
            username="otra", email="otra@example.com"
        )
        other_chore = self.create_chore(name="Ajena", assignee=other_user)
        Completion.objects.create(chore=own_chore, completed_by=self.participant)
        Completion.objects.create(chore=other_chore, completed_by=other_user)
        self.client.force_login(self.participant)

        response = self.client.get(reverse("history_list"))

        self.assertContains(response, "Propia")
        self.assertNotContains(response, "Ajena")

    def test_administrator_can_view_complete_history(self):
        chore = self.create_chore()
        Completion.objects.create(chore=chore, completed_by=self.participant)
        self.client.force_login(self.administrator)

        response = self.client.get(reverse("history_list"))

        self.assertContains(response, chore.name)

    def test_monthly_recurrence_preserves_anchor_day(self):
        chore = self.create_chore(
            frequency=Chore.Frequency.MONTHLY,
            next_due_date=date(2026, 1, 31),
        )

        chore.advance_after_completion(date(2026, 1, 31))
        chore.save()
        self.assertEqual(chore.next_due_date, date(2026, 2, 28))
        self.assertEqual(chore.recurrence_anchor_day, 31)

        chore.advance_after_completion(date(2026, 2, 28))

        self.assertEqual(chore.next_due_date, date(2026, 3, 31))

    def test_repeated_submission_does_not_duplicate_occurrence(self):
        chore = self.create_chore(
            frequency=Chore.Frequency.WEEKLY,
            next_due_date=date(2026, 9, 1),
        )
        self.client.force_login(self.participant)
        payload = {"note": "Listo", "scheduled_for": "2026-09-01"}

        with patch(
            "apps.chores.views.timezone.localdate",
            return_value=date(2026, 9, 8),
        ):
            self.client.post(reverse("chore_complete", args=[chore.pk]), payload)
            self.client.post(reverse("chore_complete", args=[chore.pk]), payload)

        chore.refresh_from_db()
        self.assertEqual(Completion.objects.filter(chore=chore).count(), 1)
        self.assertEqual(chore.next_due_date, date(2026, 9, 15))

    def test_pending_filters_by_overdue_status_and_zone(self):
        other_zone = Zone.objects.create(name="Baño")
        overdue = self.create_chore(
            name="Vencida",
            next_due_date=date(2026, 9, 7),
        )
        self.create_chore(
            name="Tarea futura",
            zone=other_zone,
            next_due_date=date(2026, 9, 9),
        )
        self.client.force_login(self.participant)

        with patch(
            "apps.chores.views.timezone.localdate",
            return_value=date(2026, 9, 8),
        ):
            response = self.client.get(
                reverse("pending_chore_list"),
                {"status": "overdue", "zone": str(self.zone.pk)},
            )

        self.assertContains(response, overdue.name)
        self.assertContains(response, "Vencida")
        self.assertNotContains(response, "Tarea futura")

    def test_history_filters_by_zone_for_administrator(self):
        other_zone = Zone.objects.create(name="Baño")
        kitchen_chore = self.create_chore(name="Limpiar cocina")
        bathroom_chore = self.create_chore(name="Trapear baño", zone=other_zone)
        Completion.objects.create(
            chore=kitchen_chore,
            completed_by=self.participant,
            scheduled_for=kitchen_chore.next_due_date,
        )
        Completion.objects.create(
            chore=bathroom_chore,
            completed_by=self.participant,
            scheduled_for=bathroom_chore.next_due_date,
        )
        self.client.force_login(self.administrator)

        response = self.client.get(
            reverse("history_list"), {"zone": str(self.zone.pk)}
        )

        self.assertContains(response, kitchen_chore.name)
        self.assertNotContains(response, bathroom_chore.name)

    def test_daily_recurrence_advances_one_day(self):
        chore = self.create_chore(
            frequency=Chore.Frequency.DAILY,
            next_due_date=date(2026, 9, 10),
        )

        chore.advance_after_completion(date(2026, 9, 10))

        self.assertEqual(chore.next_due_date, date(2026, 9, 11))

    def test_monthly_recurrence_handles_leap_year(self):
        chore = self.create_chore(
            frequency=Chore.Frequency.MONTHLY,
            next_due_date=date(2028, 1, 31),
        )

        chore.advance_after_completion(date(2028, 1, 31))
        chore.save()
        self.assertEqual(chore.next_due_date, date(2028, 2, 29))

        chore.advance_after_completion(date(2028, 2, 29))

        self.assertEqual(chore.next_due_date, date(2028, 3, 31))

    def test_completion_rejects_a_different_user(self):
        chore = self.create_chore()
        other_user = User.objects.create_user(
            username="otra", email="otra@example.com"
        )
        completion = Completion(
            chore=chore,
            completed_by=other_user,
            scheduled_for=chore.next_due_date,
        )

        with self.assertRaises(ValidationError):
            completion.full_clean()

    def test_state_change_without_csrf_token_is_rejected(self):
        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.force_login(self.administrator)

        response = csrf_client.post(reverse("zone_create"), {"name": "Sala"})

        self.assertEqual(response.status_code, 403)
        self.assertFalse(Zone.objects.filter(name="Sala").exists())
