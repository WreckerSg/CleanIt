from django.contrib import admin

from .models import Chore, Zone


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
