from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=255)
    confirmpassword = models.CharField(max_length=255)
    otp=models.CharField(max_length=6,null=True,blank=True)

    def __str__(self):
        return self.username

