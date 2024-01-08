from django.shortcuts import render,redirect

def index(request):
    return render(request, 'main/index.html') ;

def login(request):
    return render(request, 'main/login.html') ;

def register(request):
    return render(request, 'main/register.html') ;

def home(request):
    return render(request, 'main/home.html') ; 

def booking(request):
    return render(request, 'main/booking.html') ;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

def tariff(request):
    return render(request, 'main/tariff.html') ;

def offer(request):
    return render(request, 'main/offer.html') ;

def location(request):
    return render(request, 'main/location.html') ;

def contact(request):
    return render(request, 'main/contact.html') ;

def about(request):
    return render(request, 'main/about.html') ;

def privacy(request):
    return render(request, 'main/privacy.html') ;

def tc(request):
    return render(request, 'main/tc.html') ;

def help(request):
    return render(request, 'main/help.html') ;
# Create your views here.
