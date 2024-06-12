from django.urls import path
from . import views
from .views import RestaurantListView, search_restaurants, dashboard, create_restaurant, update_restaurant, update_menu, update_photo, restaurant_detail, customer_data, generate_report, trend_analysis

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('', views.home, name='home'),
    path('search/', search_restaurants, name='search_restaurants'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_restaurant, name='create_restaurant'),
    path('update/<int:pk>/', update_restaurant, name='update_restaurant'),
    path('update/<int:pk>/menu/', update_menu, name='update_menu'),
    path('update/<int:pk>/photo/', update_photo, name='update_photo'),
    path('restaurant/<int:pk>/', restaurant_detail, name='restaurant_detail'),
    path('customer-data/', customer_data, name='customer_data'),
    path('trend-analysis/', trend_analysis, name='trend_analysis'),
    path('generate-report/', generate_report, name='generate_report'),
]
