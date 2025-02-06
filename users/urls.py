from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Je to pro autentizaci

urlpatterns = [
    path('studenti', views.students_list, name='students'),
    path('uzivatele', views.users_list, name='users'),
]
