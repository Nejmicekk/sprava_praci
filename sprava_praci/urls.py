from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),  # Přidali jsme naše URL z aplikace events
    path('uzivatele/', include('users.urls')),
    path('login/', include('user_auth.urls')),
]