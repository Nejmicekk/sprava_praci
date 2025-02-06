from django import forms
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']  # Pole, která chceme ve formuláři


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Přidáme pole pro e-mail

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]