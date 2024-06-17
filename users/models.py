from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('Customer', 'Customer'),
        ('Restaurant Manager', 'Restaurant Manager'),
        ('Marketing', 'Marketing'),
        ('Staff', 'Staff'), # Aktuell ungenutzt, aber für Scalability bereits implementiert. So kann es bei potentiellen zukünftigen Bedarf genutzt werden
    ]
    role = models.CharField(max_length=25, choices=USER_ROLES, default='Customer')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Mapping von Rolle zu Gruppe
        role_to_group = {
            'Customer': 'Customer',
            'Restaurant Manager': 'Restaurant Manager',
            'Marketing': 'Marketing',
            'Staff': 'Staff',
        }

        if self.role in role_to_group:
            group_name = role_to_group[self.role]
            group, created = Group.objects.get_or_create(name=group_name)

            # Füge den Benutzer der neuen Gruppe hinzu
            self.groups.add(group)

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    preferences = models.TextField(blank=True)  # Dining preferences

    def __str__(self):
        return self.user.username
    