from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    foodtype = models.CharField(max_length=100)
    description = models.TextField()
    opening_hours = models.CharField(max_length=255)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='restaurants')

    def __str__(self):
        return self.name