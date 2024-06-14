

from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.table_list, name='table_list'),
   
  path('seat-plan/', views.seat_plan, name='seat_plan')

]
