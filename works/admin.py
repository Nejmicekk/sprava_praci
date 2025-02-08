from django.contrib import admin
from .models import Work

class WorkAdmin(admin.ModelAdmin):
    # Zobrazení atributů v adminu
    list_display = ("nazev", "popis", "navrhovatel", "schvaleno", "zpracovatel")

    # Co se zabrazuje v editu v adminu
    fieldsets = (
        (None, {"fields": ("nazev", "popis", "schvaleno")}),
        ("Uzivatele", {"fields": ("navrhovatel", "zpracovatel")}),
    )

    # Jaké atributy se zobrazí při přidávání nové práce
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("navrh", "popis", "schvaleno", "navrhovatel", "zpracovatel"),
        }),
    )

admin.site.register(Work, WorkAdmin)