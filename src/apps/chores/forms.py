from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import Chore, Completion, Zone


class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ("name", "description")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_name(self):
        return self.cleaned_data["name"].strip()


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ("name", "description", "zone", "assignee", "frequency", "next_due_date")
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "next_due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        zone_filter = Q(is_active=True)
        assignee_filter = Q(is_active=True)
        if self.instance.pk:
            zone_filter |= Q(pk=self.instance.zone_id)
            assignee_filter |= Q(pk=self.instance.assignee_id)
        self.fields["zone"].queryset = Zone.objects.filter(zone_filter).order_by("name")
        self.fields["assignee"].queryset = get_user_model().objects.filter(
            assignee_filter
        ).order_by("first_name", "username")

    def clean_name(self):
        return self.cleaned_data["name"].strip()

    def clean_zone(self):
        zone = self.cleaned_data["zone"]
        if not zone.is_active and zone.pk != self.instance.zone_id:
            raise forms.ValidationError("Seleccione una zona activa.")
        return zone

    def clean_assignee(self):
        assignee = self.cleaned_data["assignee"]
        if not assignee.is_active and assignee.pk != self.instance.assignee_id:
            raise forms.ValidationError("Seleccione una persona activa.")
        return assignee

    def save(self, commit=True):
        chore = super().save(commit=False)
        if "next_due_date" in self.changed_data:
            chore.recurrence_anchor_day = chore.next_due_date.day
        if commit:
            chore.save()
        return chore


class CompletionForm(forms.ModelForm):
    scheduled_for = forms.DateField(widget=forms.HiddenInput)

    class Meta:
        model = Completion
        fields = ("note", "scheduled_for")
        widgets = {
            "note": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Opcional: agrega una observación o evidencia.",
                }
            ),
        }
