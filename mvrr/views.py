from django.shortcuts import render,redirect

def index(request):
    return render(request, 'main/index.html') ;

def login(request):
    return render(request, 'main/login.html') ;

def register(request):
    return render(request, 'main/register.html') ;
# Create your views here.
