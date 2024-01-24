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

    
# class kyc(models.Model):
#     userid = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     licenseno = models.CharField(max_length=15, null=False)
#     idno = models.CharField(max_length=15, null=False)
    
#     @property
#     def userid(self):
#         return self.userid.userid
    
    