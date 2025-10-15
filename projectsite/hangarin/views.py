from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from hangarin.models import Priority

class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"