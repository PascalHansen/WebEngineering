from django import forms
from .models import Restaurant, Menu, Photo

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'cuisine', 'description', 'contact_info', 'opening_hours', 'next_available_reservation']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['item_name', 'description', 'price']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']
