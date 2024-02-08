from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

class UserProfile(models.Model):
    userid = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=15, null=False)
    lname = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    is_host = models.IntegerField(default=0)  # New field for host

    def __str__(self):
        return self.user.username

    
class KYCData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    licenseno = models.CharField(max_length=20)
    idno = models.CharField(max_length=20)
    licensepic = models.ImageField(upload_to='kyc_uploads/')
    idpic = models.ImageField(upload_to='kyc_uploads/')

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.user.username}"
    
    
class BikeData(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # bike = models.OneToOneField(User, on_delete=models.CASCADE)
    bikeid = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    onrname = models.CharField(max_length=50)
    regno = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    bikename = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    chassis_no = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    dop = models.DateField(blank=True, null=True)
    bikepic = models.ImageField(upload_to='bike_uploads/')
    biketype = models.CharField(max_length=20, choices=[('CLASSIC', 'Classic'), ('STREET BIKE', 'Street Bike'), ('COMMUTER', 'Commuter'), ('SPORTS BIKE', 'Sports Bike'), ('CHAPRI BIKE', 'Chapri Bike')], default='CLASSIC')
    bookedat=models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return f"{self.onrname} - {self.user.username}"
    


class BookingData(models.Model):
    bookingid = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(BikeData, on_delete=models.CASCADE)
    # onrname = models.CharField(max_length=50)
    # regno = models.CharField(max_length=50)
    # company = models.CharField(max_length=50)
    # bikename = models.CharField(max_length=50)
    # color = models.CharField(max_length=50)
    # chassis_no = models.CharField(max_length=50)
    # price = models.CharField(max_length=20)
    # dop = models.DateField(blank=True, null=True)
    # bikepic = models.ImageField(upload_to='bike_uploads/')
    # biketype = models.CharField(max_length=20, choices=[('CLASSIC', 'Classic'), ('STREET BIKE', 'Street Bike'), ('COMMUTER', 'Commuter'), ('SPORTS BIKE', 'Sports Bike'), ('CHAPRI BIKE', 'Chapri Bike')], default='CLASSIC')
    bookedat=models.DateTimeField(default=datetime.datetime.now())
    # booking_time = models.DateTimeField(auto_now_add=True)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    dropoff_date = models.DateField()
    dropoff_time = models.TimeField()
    duration = models.CharField(max_length=50,null=True,blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def _str_(self):
        return f"Booking #{self.pk} - {self.user.username} - {self.bike.bikename}"
    