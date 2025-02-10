from django.urls import path
from .views import WorkDetailView

urlpatterns = [
    path('prace/<int:pk>', WorkDetailView.as_view(), name='work_detail')
]
