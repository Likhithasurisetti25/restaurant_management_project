from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user=models.OneToOneFieldUser,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    def__str__(self):
        return self.user.username

# Create your models here.
