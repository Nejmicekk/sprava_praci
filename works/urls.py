from django.urls import path
from .views import work_detail

urlpatterns = [
    path('prace/<int:pk>', work_detail, name='work_detail')
]
