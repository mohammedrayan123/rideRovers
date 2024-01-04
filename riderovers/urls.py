"""
URL configuration for riderovers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mvrr.views import index,login,register,tariff,offer,location,contact,about,privacy,tc,help

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("main/login.html",view=login,name="login"),
    path("main/register.html",view=register,name="register"),
    path("main/tariff.html",view=tariff,name="tariff"),
    path("main/offer.html",view=offer,name="offer"),
    path("main/location.html",view=location,name="location"),
    path("main/contact.html",view=contact,name="contact"),
    path("main/about.html",view=about,name="about"),
    path("main/privacy.html",view=privacy,name="privacy"),
    path("main/tc.html",view=tc,name="tc"),
    path("main/help.html",view=help,name="help"),

]
