from django.shortcuts import render,redirect

def index(request):
    return render(request, 'main/index.html') ;

def login(request):
    return render(request, 'main/login.html') ;

def register(request):
    return render(request, 'main/register.html') ;

def tariff(request):
    return render(request, 'main/tariff.html') ;

def offers(request):
    return render(request, 'main/offers.html') ;
# Create your views here.
