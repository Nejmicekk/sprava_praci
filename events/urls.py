from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Je to pro autentizaci

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('events/', views.event_list, name='event_list'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]




