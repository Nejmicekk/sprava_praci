from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def students_list(request):
    users = CustomUser.objects.all()[1:]
    #jednicka zajistuje, aby se nevypsala prvni prazdna
    return render(request, 'studenti.html', {'users': users})

@login_required
def users_list(request):
    users = CustomUser.objects.all()[1:]
    #jednicka zajistuje, aby se nevypsala prvni prazdna
    return render(request, 'uzivatele.html', {'users': users})