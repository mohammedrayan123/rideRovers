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
from mvrr.views import index,login,hlogin,register,hregister,home,profile,kyc,tariff,offer,location,contact,about,privacy,tc,help,booking

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",view=login,name="login"),
    path("main/hlogin",view=hlogin,name="hlogin"),
    path("main/index",index,name="index"),
    path("main/register",view=register,name="register"),
    path("main/hregister",view=hregister,name="hregister"),
    path("main/home",view=home,name="home"),
    path("main/profile",view=profile,name="profile"),
    path("main/kyc",view=kyc,name="kyc"),
    path("main/booking",view=booking,name="booking"),
    path("main/tariff",view=tariff,name="tariff"),
    path("main/offer",view=offer,name="offer"),
    path("main/location",view=location,name="location"),
    path("main/contact",view=contact,name="contact"),
    path("main/about",view=about,name="about"),
    path("main/privacy",view=privacy,name="privacy"),
    path("main/tc",view=tc,name="tc"),
    path("main/help",view=help,name="help"),

]
