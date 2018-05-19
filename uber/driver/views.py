from django.http  import HttpResponse
from django.shortcuts import render
from .models import Driver

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')

def d_profile(request):
    return render(request, 'driver-profile.html')

def home2(request):
    return render(request, 'home2.html')

def p_profile(request):
    return render(request, 'passenger-profile.html')

