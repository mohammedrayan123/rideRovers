from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=15, null=False)
    lname = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=25, null=False)
    gender = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    # password = forms.CharField(widget=forms.PasswordInput)

    def _str_(self):
        return self.user.username