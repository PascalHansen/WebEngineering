from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Booking, Menu, Photo
from users.models import CustomerProfile, CustomUser
from reviews.models import Feedback
from django.contrib.auth.decorators import permission_required
from .forms import RestaurantForm, MenuForm, PhotoForm
from django.db.models import Count
import datetime
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Create your views here.
def home(request):
    return render(request, 'restaurants/home.html')

def search_restaurants(request):
    query = request.GET.get('query')
    location = request.GET.get('location')
    cuisine = request.GET.get('cuisine')
    availability = request.GET.get('availability')
    
    restaurants = Restaurant.objects.all()

    if query:
        restaurants = restaurants.filter(name__icontains=query)
    if location:
        restaurants = restaurants.filter(location__icontains=location)
    if cuisine:
        restaurants = restaurants.filter(cuisine__icontains=cuisine)
    if availability:
            restaurants = restaurants.filter(next_available_reservation__gte=availability)


    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/search_results.html', context)

# Dashboard einsehen
@permission_required('restaurants.owner_dashboard', raise_exception=True)
def dashboard(request):
    restaurants = Restaurant.objects.filter(owner=request.user)
    return render(request, 'restaurants/owner_dashboard.html', {'restaurants': restaurants})
    

# Restaurant erstellen
@permission_required('restaurants.create_restaurant', raise_exception=True)
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            return redirect('dashboard')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/create_restaurant.html', {'form': form})

# Restaurant updaten
@permission_required('restaurants.update_restaurant', raise_exception=True)
def update_restaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/update_restaurant.html', {'form': form})

# Menü updaten
@permission_required('restaurants.update_menu', raise_exception=True)
def update_menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            return redirect('dashboard')
    else:
        form = MenuForm()
    return render(request, 'restaurants/update_menu.html', {'form': form})

# Foto updaten
@permission_required('restaurants.update_photo', raise_exception=True)
def update_photo(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        if 'upload' in request.POST:
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                photo = form.save(commit=False)
                photo.restaurant = restaurant
                photo.save()
                return redirect('update_photo', pk=pk)
        elif 'delete' in request.POST:
            photo_id = request.POST.get('photo_id')
            photo = get_object_or_404(Photo, id=photo_id)
            photo.image.delete()  # Löscht die Datei vom Speichermedium
            photo.delete()        # Löscht den Datenbankeintrag
            return redirect('update_photo', pk=pk)
    else:
        form = PhotoForm()
    
    photos = Photo.objects.filter(restaurant=restaurant)
    return render(request, 'restaurants/update_photo.html', {'form': form, 'photos': photos, 'pk': pk})

# Details einsehen
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menus = Menu.objects.filter(restaurant=restaurant)
    photos = Photo.objects.filter(restaurant=restaurant)
    return render(request, 'restaurants/restaurant_detail.html', {
        'restaurant': restaurant,
        'menus': restaurant.menus.all(),
        'photos': restaurant.photos.all(),
        'reviews': restaurant.reviews.all()
    })

# Restaurants löschen
@permission_required('restaurants.delete_restaurant', raise_exception=True)
def delete_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    
    if restaurant.owner == request.user:
        if request.method == "POST":
           restaurant.delete()
           messages.success(request, "Restaurant deleted successfully.")
           return redirect('dashboard')
    else:
        return render(request, 'restaurants/access_denied.html')
    
    return render(request, 'restaurants/delete_restaurant_confirm.html', {'restaurant': restaurant})

# Kundendaten einsehen
@permission_required('restaurants.customer_data', raise_exception=True)
def customer_data(request):
    today = datetime.date.today()
    bookings = Booking.objects.all()
    feedbacks = Feedback.objects.all()
    demographics = CustomerProfile.objects.values('age', 'gender').annotate(count=Count('user'))

    return render(request, 'restaurants/customer_data.html', {
        'bookings': bookings,
        'feedbacks': feedbacks,
        'demographics': demographics
    })

# Trends einsehen
@permission_required('restaurants.trend_analysis', raise_exception=True)
def trend_analysis(request):
    today = datetime.date.today()
    popular_times = Booking.objects.values('date').annotate(count=Count('id')).order_by('-count')
    popular_items = Booking.objects.values('restaurant__menus__item_name').annotate(count=Count('restaurant__menus')).order_by('-count')
    peak_seasons = Booking.objects.values('date__month').annotate(count=Count('id')).order_by('-count')
    feedback_themes = Feedback.objects.values('comment').annotate(count=Count('id')).order_by('-count')

    return render(request, 'restaurants/trend_analysis.html', {
        'popular_times': popular_times,
        'popular_items': popular_items,
        'peak_seasons': peak_seasons,
        'feedback_themes': feedback_themes
    })

# Berichte erstellen (??)
@permission_required('restaurants.generate_report', raise_exception=True)
def generate_report(request):
    # Muss noch implementiert werden
    return render(request, 'restaurants/generate_report.html')

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurant_list.html'
    context_object_name = 'restaurants'

def permission_denied_view(request):
    return render(request, 'restaurants/access_denied.html', status=403)