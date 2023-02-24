from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = [
        "id",
        "username",
        "email",
    ]
    list_filter = ["email"]
    ordering = []
    filter_horizontal = []
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                )
            },
        ),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )
