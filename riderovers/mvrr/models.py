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
    is_host = models.BooleanField(default=False)  # New field for host

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
    
    
# class bikedata(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     onrname = models.CharField(max_length=50)
#     regno = models.CharField(max_length=50)
#     company = models.CharField(max_length=50)
#     bikename = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     chessis_no = models.CharField(max_length=50)
#     price = models.CharField(max_length=20)
#     dop = models.DateField(blank=True, null=True)
#     bikepic = models.ImageField(upload_to='kyc_uploads/')

#     def __str__(self):
#         return f"{self.fname} {self.lname} - {self.user.username}"