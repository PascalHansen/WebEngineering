from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm): # Muss noch angepasst werden wenn Mohammad fertig ist
    class Meta:
        model = Reservations
        fields = ['restaurant', 'date', 'time', 'party_size']

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('guest_name', 'reservation_date', 'reservation_time', 'guest_count', 'special_requests','table')
