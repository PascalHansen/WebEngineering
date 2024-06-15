from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.table_list, name='table_list'),
    path('seat-plan/', views.seat_plan, name='seat_plan'),
    path('', views.promotion_list, name='promotion_list'),
    path('promotion/new/', views.promotion_create, name='promotion_create'),
    path('promotion/<int:pk>/edit/', views.promotion_edit, name='promotion_edit'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dish/new/', views.dish_create, name='dish_create'),
    path('dish/<int:pk>/edit/', views.dish_edit, name='dish_edit'),
]