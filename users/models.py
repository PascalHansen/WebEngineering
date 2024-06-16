from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser, AbstractBaseUser, PermissionsMixin):
    USER_ROLES = [
        ('customer', 'Customer'),
        ('manager', 'Restaurant Manager'),
        ('marketing', 'Marketing'),
        ('staff', 'Staff'), # Aktuell ungenutzt, aber für Scalability bereits implementiert. So kann es bei potentiellen zukünftigen Bedarf genutzt werden
    ]
    role = models.CharField(max_length=25, choices=USER_ROLES, default='customer')

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    preferences = models.TextField(blank=True)  # Dining preferences

    def __str__(self):
        return self.user.username
    