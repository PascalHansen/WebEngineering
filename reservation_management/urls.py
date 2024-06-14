

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  
    
    path('', views.reservation_list, name='reservation_list'),
    path('add/', views.reservation_add, name='reservation_add'),
    path('edit/<int:pk>/', views.reservation_edit, name='reservation_edit'),
    path('delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),
]




