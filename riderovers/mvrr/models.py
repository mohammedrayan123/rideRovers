from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
   
    addr = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.user.username