from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/dashboard/")  # Přesměrování přihlášeného uživatele
        return super().get(request, *args, **kwargs)

def not_logged_in(request):
    return render(request, 'not_logged_in.html')