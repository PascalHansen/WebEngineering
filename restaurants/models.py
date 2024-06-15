from django.db import models
from users.models import CustomUser

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    description = models.TextField()
    opening_hours = models.CharField(max_length=100, blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    next_available_reservation = models.DateTimeField()
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='restaurants')

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name

class Photo(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='restaurants/restaurant_photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.restaurant.name}"
    
class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"{self.customer.username} booking at {self.restaurant.name}"
    