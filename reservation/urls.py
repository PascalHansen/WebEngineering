"""
URL configuration for reservation project.

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
from django.urls import include, path
from django.views.generic import TemplateView
from management import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('reviews/', include('reviews.urls')),
    path('reservations/', include('reservations.urls')),
    path('management/', include('management.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('', include('restaurants.urls')), 
    path('management/', views.table_list, name='table_list'),
    path('management/<int:table_id>/change_status/', views.change_status, name='change_status'),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)