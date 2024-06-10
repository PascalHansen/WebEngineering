from django.urls import path
from .views import book_reservation

urlpatterns = [
    path('book/<int:restaurant_id>/', book_reservation, name='book_reservation'),
]