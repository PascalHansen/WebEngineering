
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('guest_name', 'reservation_date', 'reservation_time', 'guest_count', 'special_requests','table')
