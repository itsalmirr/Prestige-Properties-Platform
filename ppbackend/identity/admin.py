from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Identity


class IdentityAdminConfig(UserAdmin):
    # Display the following fields in the admin panel
    list_display = (
        "id",
        "email",
        "username",
        "full_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_filter = ("email", "is_staff", "is_superuser", "is_active")
    search_fields = ("email", "username")
    ordering = ("-start_date",)
    fieldsets = (
        (None, {"fields": ("avatar", "email", "password")}),
        (
            "Personal info",
            {"fields": ("username", "full_name", "start_date")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "20"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }


admin.site.register(Identity, IdentityAdminConfig)
