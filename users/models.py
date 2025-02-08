from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
import unidecode

class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=100, blank=False)
    prijmeni = models.CharField(max_length=100, blank=False)
    
    trida = models.CharField(max_length=3)

    class Types(models.TextChoices):
        student = "student", "Student"
        ucitel = "ucitel", "Ucitel"
        admin = "admin", "Admin"

    role = models.CharField(
        max_length=15,
        choices=Types.choices,
        default=Types.student
    )

    class Genders(models.TextChoices):
        male = "muz", "Žena"
        female = "zena", "Muž"
        jine = "jine", "Nechci uvádět"

    pohlavi = models.CharField(
        max_length=4,
        choices=Genders.choices,
        default=Genders.jine
    )

    def save(self, *args, **kwargs):
        if self.jmeno and self.prijmeni:
            jmeno = unidecode.unidecode(self.jmeno.lower().strip())
            prijmeni = unidecode.unidecode(self.prijmeni.lower().strip())

            self.username = f"{prijmeni}.{jmeno}"
            self.email = f"{prijmeni}.{jmeno}@purkynka.cz"
        super().save(*args, **kwargs)

    pass