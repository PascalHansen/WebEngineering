from django.db import models

# Create your models here.

class Reservations(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f'Reservation for {self.party_size} at {self.restaurant.name} on {self.date} at {self.time}'