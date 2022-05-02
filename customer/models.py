from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=True,editable=False)
    prefftime1 = models.TimeField(null=True)
    prefftime2 = models.TimeField(null=True)
    prefftime3 = models.TimeField(null=True)
    bit = models.CharField(max_length=10,null=True)
    alloted_time=models.CharField(max_length=10,editable=True)
    approved= models.BooleanField(default=False,editable=True)
    def __str__(self):
        return self.user.first_name
