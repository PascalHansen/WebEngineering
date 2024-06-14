
from django.db import models

class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    STATUS_CHOICES = [
        ('Frei', 'Frei'),
        ('Reserviert', 'Reserviert'),
        ('Außer Betrieb', 'Außer Betrieb'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Tisch {self.table_number}"
