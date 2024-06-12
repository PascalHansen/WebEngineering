from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Menu, Photo, Booking, Feedback, CustomerProfile 
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RestaurantForm, MenuForm, PhotoForm
from django.db.models import Count, Avg
import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')

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
    return render(request, 'search_results.html', context)

@login_required
def dashboard(request):
    restaurants = Restaurant.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'restaurants': restaurants})

@login_required
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            return redirect('dashboard')  # Stellen Sie sicher, dass Sie diese URL in Ihrem Projekt definiert haben
    else:
        form = RestaurantForm()
    return render(request, 'create_restaurant.html', {'form': form})

@login_required
def update_restaurant(request, pk):
    restaurant = Restaurant.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'update_restaurant.html', {'form': form})

@login_required
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
    return render(request, 'update_menu.html', {'form': form})

@login_required
def update_photo(request, pk):
    restaurant = Restaurant.objects.get(pk=pk, owner=request.user)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.restaurant = restaurant
            photo.save()
            return redirect('dashboard')
    else:
        form = PhotoForm()
    return render(request, 'update_photo.html', {'form': form})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'menus': restaurant.menus.all(),
        'photos': restaurant.photos.all(),
        'reviews': restaurant.reviews.all()
    })

def is_marketing(user):
    return user.groups.filter(name='Marketing').exists()

@user_passes_test(is_marketing)
def customer_data(request):
    today = datetime.date.today()
    bookings = Booking.objects.all()
    feedbacks = Feedback.objects.all()
    demographics = CustomerProfile.objects.values('age', 'gender').annotate(count=Count('user'))

    return render(request, 'customer_data.html', {
        'bookings': bookings,
        'feedbacks': feedbacks,
        'demographics': demographics
    })

@user_passes_test(is_marketing)
def trend_analysis(request):
    today = datetime.date.today()
    popular_times = Booking.objects.values('date').annotate(count=Count('id')).order_by('-count')
    popular_items = Booking.objects.values('restaurant__menus__item_name').annotate(count=Count('restaurant__menus')).order_by('-count')
    peak_seasons = Booking.objects.values('date__month').annotate(count=Count('id')).order_by('-count')
    feedback_themes = Feedback.objects.values('comment').annotate(count=Count('id')).order_by('-count')

    return render(request, 'trend_analysis.html', {
        'popular_times': popular_times,
        'popular_items': popular_items,
        'peak_seasons': peak_seasons,
        'feedback_themes': feedback_themes
    })

@user_passes_test(is_marketing)
def generate_report(request):
    # Implement custom report generation logic here
    return render(request, 'generate_report.html')