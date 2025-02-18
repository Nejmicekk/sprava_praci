from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def students_list(request):
    users = CustomUser.objects.all()[1:]
    #jednicka zajistuje, aby se nevypsala prvni prazdna
    return render(request, 'studenti.html', {'users': users})

@login_required(login_url="/login/")
def users_list(request):
    query = request.GET.get("q", "")  # Získáme hodnotu z vyhledávacího pole

    if query:
        users = CustomUser.objects.filter(jmeno__icontains=query) | CustomUser.objects.filter(prijmeni__icontains=query)
    else:
        users = CustomUser.objects.all()[1:]

    return render(request, "uzivatele.html", {"users": users, "query": query})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="/login/")
def odstranit_uzivatele(request, pk):
    if not request.user.role == "admin":
        messages.error(request, "Nemáte oprávnění mazat uživatele.")
    else:
        user = get_object_or_404(CustomUser, pk=pk)

        if user == request.user:
            messages.error(request, "Nemůžete smazat vlastní účet.")
        elif user.role == "admin":
            messages.error(request, "Nemůžete smazat administrátora.")
        else:
            user.delete()
            messages.success(request, f"Uživatel {user.username} byl úspěšně odstraněn.")

    return redirect("uzivatele")