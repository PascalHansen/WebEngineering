from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('customer', 'Customer'),
        ('owner', 'Owner'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=10, choices=USER_ROLES, default='customer')

    def __str__(self):
        return self.username
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    preferences = models.TextField(blank=True)  # Dining preferences

    def __str__(self):
        return self.user.username
    