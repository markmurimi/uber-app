from django.http  import HttpResponse
from django.shortcuts import render
from .models import Driver
from django.contrib.auth.decorators import login_required


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def d_profile(request):
    return render(request, 'driver-profile.html')

@login_required(login_url='/accounts/login/')
def home2(request):
    return render(request, 'home2.html')

@login_required(login_url='/accounts/login/')
def p_profile(request):
    return render(request, 'passenger-profile.html')

