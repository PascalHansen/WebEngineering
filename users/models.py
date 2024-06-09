from django.contrib.auth.models import AbstractUser
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