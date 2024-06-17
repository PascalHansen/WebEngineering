#from django.contrib import admin
#from .models import Reservations

#@admin.register(Reservations)
#class ReservationsAdmin(admin.ModelAdmin):
#    list_display = ('id', 'restaurant', 'user', 'date', 'time', 'party_size', 'status')

from django.apps import AppConfig

class ReservationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'
