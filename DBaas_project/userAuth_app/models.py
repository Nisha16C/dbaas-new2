# models.py

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
