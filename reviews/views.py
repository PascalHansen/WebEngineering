from django.views.generic import ListView
from .models import Review

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10  # Seitenpaginierung, falls viele Bewertungen vorhanden sind