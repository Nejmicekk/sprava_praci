# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("username", "jmeno", "prijmeni", "role", "trida", "email", "is_staff", "is_active")  # Zobrazení uživatelů v adminu

    fieldsets = (
        (None, {"fields": ("username", "password", "email")}),
        ("Personal info", {"fields": ("jmeno", "prijmeni", "trida")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "role")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (  # Nastavuje pole při vytváření nového uživatele
        (None, {
            "classes": ("wide",),
            "fields": ("jmeno", "prijmeni", "email", "trida", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)

print("hello world!!!")