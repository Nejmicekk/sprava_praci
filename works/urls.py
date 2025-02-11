from django.urls import path
from .views import *

urlpatterns = [
    path('navrh_prace/<int:pk>', work_detail, name='work_detail'),
    path("schvalit/<int:pk>/", schvalit_praci, name="schvalit_praci"),
    path("zamitnout_praci/<int:pk>/", zamitnout_praci, name="zamitnout_praci"),
]
