from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10  # Seitenpaginierung, falls viele Bewertungen vorhanden sind

@permission_required('reviews.add_review', raise_exception=True)
def create_review(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant_id = restaurant_id
            review.save()
            return redirect('restaurant_detail', pk=restaurant_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

@permission_required('reviews.delete_review', raise_exception=True)
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if review.user == request.user:  # Nur der Ersteller kann löschen
        review.delete()
        return redirect('restaurant_detail', pk=review.restaurant_id)
    else:
        return render(request, 'reviews/forbidden.html')
    
def permission_denied_view(request):
    return render(request, 'reviews/access_denied.html', status=403)