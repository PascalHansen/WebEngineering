from django.db import models
from users.models import CustomUser
from restaurants.models import Restaurant

# Create your models here.

class Review(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.restaurant.name}'

    class Meta:
        ordering = ['-date_posted']

class Feedback(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.customer.username} for {self.restaurant.name}"