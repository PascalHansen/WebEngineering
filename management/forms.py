from django import forms
from .models import Promotion, Dish, SpecialOffer

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'discount', 'special_menu_item', 'loyalty_points', 'start_date', 'end_date', 'is_active']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'loyalty_points_required', 'is_available']

class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialOffer
        fields = ['title', 'description', 'discount_rate', 'start_date', 'end_date', 'terms_and_conditions']