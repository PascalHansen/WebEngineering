from django.db import models

# Tisch
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

# Promotions Models  
class Promotion(models.Model):
    title = models.CharField("Titel", max_length=100)
    description = models.TextField("Beschreibung")
    discount = models.DecimalField("Rabatt", max_digits=5, decimal_places=2, default=0.0)
    special_menu_item = models.CharField("Spezialmenüartikel", max_length=100, blank=True, null=True)
    loyalty_points = models.IntegerField("Treuepunkte", default=0)
    start_date = models.DateField("Startdatum")
    end_date = models.DateField("Enddatum")
    is_active = models.BooleanField("Aktiv", default=True)

    def __str__(self):
        return self.title

class Dish(models.Model):
    name = models.CharField("Gerichtname", max_length=100)
    description = models.TextField("Beschreibung")
    loyalty_points_required = models.IntegerField("Erforderliche Treuepunkte")
    is_available = models.BooleanField("Verfügbar", default=True)

    def __str__(self):
        return self.name