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
# from django.contrib import admin
# from django.urls import path
# from mvrr.views import index,login,hlogin,register,hregister,home,profile,kyc,tariff,offer,location,contact,about,privacy,tc,help,booking

from django.contrib import admin
from django.urls import path
from mvrr.views import *

from . import settings
from django.conf.urls. static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", user_login, name="login"),
    path("index", index, name="index"),
    path("register/",user_register, name="user_register"),
    path("logout/",logout_user, name="logout_user"),
    # path("main/hlogin",view=hlogin,name="hlogin"),
    # path("main/hregister",view=hregister,name="hregister"),
    path("home", home, name="home"),
    path("profile", profile, name="profile"),
    path("editprofile/<str:id>", edituser, name="edituser"),
    path("editprofile/<str:id>", edituser, name="edit-user"),
    path('delete/<str:id>',deleteuser,name='delete-user'),
    path("host-dashboard",view=host,name="host"),
    path("host-profile",view=hprofile,name="hprofile"),
    path("bike-registration",view=bike,name="bike"),
    path("my-bikes",view=bikelist,name="bikelist"),
    path("admin-den",view=adminboard,name="adminboard"),
    path("main/kyc",view=kyc,name="kyc"),
    path("booking/<uuid:id>", booking, name="booking-bike"),
    path('booking/bike/<uuid:id>/',booking_bike,name="booking"),
    path("tariff", tariff, name="tariff"),
    path("offer", offer, name="offer"),
    path("location", location, name="location"),
    path("contact", contact, name="contact"),
    path("about", about, name="about"),
    path("privacy", privacy, name="privacy"),
    path("tc", tc, name="tc"),
    path("help", help, name="help"),
    path("kyc_done", kyc_done, name="kyc_done"),
    path("success", success, name="success"),
    path("comingsoon", comingsoon, name="comingsoon"),
    path("admincharts", admincharts, name="admincharts"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
