from django.shortcuts import render
from .models import Atm
from django.views.generic import ListView


class AtmList(ListView):
    model = Atm
    template_name = 'home.html'
