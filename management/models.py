from django.db import models
from datetime import datetime

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
    
    class Meta:
        permissions = [
            ("table_list", "Can access table lists"),
            ("change_status", "Can change the table status"),
            ("seat_plan", "Can access the seat plan"),
        ]

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

    class Meta:
        permissions = [
            ("promotion_create", "Can create promotions"),
            ("promotion_edit", "Can edit promotions"),
        ]

# Dish / Gerichte
class Dish(models.Model):
    name = models.CharField("Gerichtname", max_length=100)
    description = models.TextField("Beschreibung")
    loyalty_points_required = models.IntegerField("Erforderliche Treuepunkte")
    is_available = models.BooleanField("Verfügbar", default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        permissions = [
            ("dish_create", "Can create dishes"),
            ("dish_edit", "Can edit dishes"),
        ]
    
# Notifications Model
class Notification(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.now)
      
    def __str__(self):
        return self.message

    class Meta:
        permissions = [
            ("get_notifications", "Can get notifications"),
            ("clear_notifications", "Can clear notifications"),
        ]

# Für Special offers
class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    terms_and_conditions = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ("special_offer", "Can create special offers"),
        ]