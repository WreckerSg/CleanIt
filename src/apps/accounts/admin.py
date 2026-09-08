from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CleanItUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "is_active")
    list_filter = ("role", "is_active", "is_staff")
    fieldsets = UserAdmin.fieldsets + (("CleanIt", {"fields": ("role",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("CleanIt", {"fields": ("email", "role")}),
    )
