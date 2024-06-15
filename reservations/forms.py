from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('date', 'time', 'party_size', 'special_requests')
