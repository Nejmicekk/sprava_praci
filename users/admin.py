from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Zobrazení atributů/sloupců v adminu
    list_display = ("username", "jmeno", "prijmeni", "email", "role", "trida", "is_staff", "is_active")

    # Co se zobrazuje když budeme editovat práci v adminu
    fieldsets = (
        (None, {"fields": ("username", "password", "email")}),
        ("Personal info", {"fields": ("jmeno", "prijmeni", "trida")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "role")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Jaké atributy se zobrazí při vytváření nového uživatele
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("jmeno", "prijmeni", "trida", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)