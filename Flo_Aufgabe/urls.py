"""
URL configuration for Flo_Aufgabe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from table_seating_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promotion/', include('promotion_management.urls')),
    path('reservation/', include('reservation_management.urls')),
    path('tables/', views.table_list, name='table_list'),
    path('', include('table_seating_management.urls')),
    path('tables/<int:table_id>/change_status/', views.change_status, name='change_status'),
    path('notifications/', include('notifications_management.urls')),

]
