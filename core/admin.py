from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUerAdmin

from core.models import MyUser


@admin.register(MyUser)
class UserAdmin(BaseUerAdmin):

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )
