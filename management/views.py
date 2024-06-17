from django.shortcuts import render, redirect
from .models import Table, Promotion, Dish, Notification, SpecialOffer
from reservations.models import Reservations
from .forms import PromotionForm, DishForm, SpecialOfferForm
from django.contrib.auth.decorators import permission_required

# Tisch Management
@permission_required('table_list', raise_exception=True)
def table_list(request):
    tables = Table.objects.all().order_by('table_number')
    return render(request, 'management/table_list.html', {'tables': tables})

@permission_required('change_status')
def change_status(request, table_id):
    table = Table.objects.get(pk=table_id)
    if request.method == 'POST':
        new_status = request.POST['status']
        table.status = new_status
        table.save()
        return redirect('table_list')
    return render(request, 'management/change_status.html', {'table': table})

@permission_required('seat_plan', raise_exception=True)
def seat_plan(request):
    tables_with_guests = {}

    tables = Table.objects.all()

    for table in tables:
        tables_with_guests[table] = []

    reservations = Reservations.objects.all()

    for reservation in reservations:
        if reservation.table in tables_with_guests:
            tables_with_guests[reservation.table].append(reservation)

    context = {
        'tables_with_guests': tables_with_guests,
    }

    return render(request, 'management/seat_plan.html', context)

# Promotion Management
def promotion_list(request):
    promotions = Promotion.objects.filter(is_active=True)
    return render(request, 'management/promotion_list.html', {'promotions': promotions})

@permission_required('promotion_create', raise_exception=True)
def promotion_create(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm()
    return render(request, 'management/promotion_form.html', {'form': form})

@permission_required('promotion_edit', raise_exception=True)
def promotion_edit(request, pk):
    promotion = Promotion.objects.get(pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'management/promotion_form.html', {'form': form})

def dish_list(request):
    dishes = Dish.objects.filter(is_available=True)
    return render(request, 'management/dish_list.html', {'dishes': dishes})

@permission_required('dish_create', raise_exception=True)
def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'management/dish_form.html', {'form': form})

@permission_required('dish_edit', raise_exception=True)
def dish_edit(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'management/dish_form.html', {'form': form})

# Notifications Management
@permission_required('get_notifications', raise_exception=True)
def notification_list(request):
    notifications = Notification.objects.all().order_by('-timestamp')
    return render(request, 'management/notification_list.html', {'notifications': notifications})

@permission_required('clear_notification', raise_exception=True)
def clear_notifications(request):
    if request.method == 'POST':
        Notification.objects.all().delete()
    
    return redirect('notification_list')

@permission_required('special_offer', raise_exception=True)
def create_special_offer(request):
    if request.method == 'POST':
        form = SpecialOfferForm(request.POST)
        if form.is_valid():
            special_offer = form.save()
            return redirect('management/special_offer.html')
    else:
        form = SpecialOfferForm()
    
    return render(request, 'management/special_offer.html', {'form': form})

def permission_denied_view(request):
    return render(request, 'management/access_denied.html', status=403)