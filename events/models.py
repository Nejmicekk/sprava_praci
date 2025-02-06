from django.db import models
from users.models import CustomUser as User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Vlastník události

    def __str__(self):
        return self.title
