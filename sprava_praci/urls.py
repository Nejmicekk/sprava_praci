from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('uzivatele/', include('users.urls')),
    path('login/', include('user_auth.urls')),
]