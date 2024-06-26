from django.db import models
from management.models import Table
from users.models import CustomUser
from restaurants.models import Restaurant  

# Create your models here.
def get_table_model():
    from management.models import Table
    return Table

class Reservations(models.Model):
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='reservations')
    date = models.DateTimeField()
    time = models.CharField(max_length=100, blank=True)
    party_size = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f'Reservation for {self.party_size} at {self.restaurant} on {self.date} at {self.time}'
    
    class Meta:
        permissions = [
            ("reservation_list", "Can view the list of reservations"),
            ("view_reservationdetail", "Can view the detail of a reservation"),
            ("change_reservation", "Can edit reservations"),
            ("add_reservation", "Can add reservations"),
            ("delete_reservation", "Can delete reservations"),
        ]