from django.http  import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')

def d_profile(request):
    return render(request, 'driver-profile.html')