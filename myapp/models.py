from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    opening_hours = models.CharField(max_length=100, blank=True)
    next_available_reservation = models.DateTimeField()

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
    image = models.ImageField(upload_to='restaurant_photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.restaurant.name}"
    
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.restaurant.name}"
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    preferences = models.TextField(blank=True)  # Dining preferences

    def __str__(self):
        return self.user.username
    
class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"{self.customer.username} booking at {self.restaurant.name}"
    
class Feedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.customer.username} for {self.restaurant.name}"