from django.db import models
from users.models import CustomUser

class Work(models.Model):
    nazev = models.CharField(max_length=255)
    popis = models.TextField()
    schvaleno = models.BooleanField(default=False)

    #pokud se uzivatel smaze, tak se smaze i navrh jeho prace
    navrhovatel  = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="navrzene_prace"
    )
    
    zpracovatel = models.OneToOneField(
        CustomUser,
        on_delete = models.SET_NULL,
        related_name="zpracovana_prace",
        null=True,
        blank=True,
        limit_choices_to={"role" : "student"}
    )

    schvalovatel  = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="schvalene_prace",
        null=True,
        blank=True,
        limit_choices_to={"role" : "ucitel"}
    )

    def __str__(self):
        return self.nazev
    
    def schvaleno_text(self):
        return "Ano" if self.schvaleno else "Ne"
