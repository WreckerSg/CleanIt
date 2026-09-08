from django.contrib import admin

from .models import Chore, Completion, Zone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ("name", "zone", "assignee", "frequency", "next_due_date", "is_active")
    list_filter = ("is_active", "frequency", "zone")
    search_fields = ("name", "description", "assignee__username")
    autocomplete_fields = ("assignee",)


@admin.register(Completion)
class CompletionAdmin(admin.ModelAdmin):
    list_display = ("chore", "completed_by", "scheduled_for", "completed_at")
    list_filter = ("completed_at",)
    search_fields = ("chore__name", "completed_by__username", "note")
    readonly_fields = ("completed_at",)
