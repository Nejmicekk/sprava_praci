from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout_user/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout_user'),
    path('not_logged_in/', views.not_logged_in, name='not_logged_in'),
]
