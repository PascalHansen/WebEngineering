from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('customer', 'Customer'),
        ('manager', 'Manager'),
    ]
    role = models.CharField(max_length=10, choices=USER_ROLES, default='customer')

    def __str__(self):
        return self.username

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    preferences = models.TextField(blank=True)  # Dining preferences

    def __str__(self):
        return self.user.username
    