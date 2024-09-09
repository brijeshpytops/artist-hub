from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return render(request, r'web\login.html')

def register_view(request):
    return render(request, r'web\register.html')

def dashboard_view(request):
    return render(request, r'web\dashboard.html')

def catalogue_view(request):
    return render(request, r'web\catalogue.html')

def profile_view(request):
    return render(request, r'web\profile.html')


