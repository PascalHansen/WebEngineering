from django.urls import path
from .views import ReviewListView, create_review, delete_review

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('create/<int:restaurant_id>/', create_review, name='create_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
]