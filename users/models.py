from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('Customer', 'Customer'),
        ('RestaurantManager', 'Restaurant Manager'),
        ('Marketing', 'Marketing'),
        ('Staff', 'Staff'), # Aktuell ungenutzt, aber für Scalability bereits implementiert. So kann es bei potentiellen zukünftigen Bedarf genutzt werden
    ]
    role = models.CharField(max_length=25, choices=USER_ROLES, default='Customer')

    def __str__(self):
        return self.username
    
    class Meta:
        permissions = [
            ("profile_view", "Can view profiles"),
        ]

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    preferences = models.TextField(blank=True)  # Dining preferences

    def __str__(self):
        return self.user.username
    