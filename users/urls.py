from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Je to pro autentizaci

urlpatterns = [
    path('studenti', views.students_list, name='students'),
    path('', views.users_list, name='uzivatele'),
    path('delete/<int:pk>/', views.odstranit_uzivatele, name="odstranit_uzivatele"),
]
