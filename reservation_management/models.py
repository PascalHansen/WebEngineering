

from django.db import models
from table_seating_management.models import Table      




class Reservation(models.Model):
    guest_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    guest_count = models.IntegerField()
    special_requests = models.TextField(blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.guest_name

  


