from django.urls import path
from . import views

urlpatterns = [
    path('', views.AtmList.as_view(), name='atm_list'),
]