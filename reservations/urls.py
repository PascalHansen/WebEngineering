from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('add/', views.reservation_add, name='reservation_add'),
    path('edit/<int:pk>/', views.reservation_edit, name='reservation_edit'),
    path('delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
]