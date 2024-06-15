from django.shortcuts import render, redirect
from .models import Table, Promotion, Dish
from reservations.models import Reservations
from .forms import PromotionForm, DishForm
from django.contrib.auth.decorators import permission_required

# Tisch Management
@permission_required('management.table_list', raise_exception=True)
def table_list(request):
    tables = Table.objects.all().order_by('table_number')
    return render(request, 'templates/table_list.html', {'tables': tables})

def change_status(request, table_id):
    table = Table.objects.get(pk=table_id)
    if request.method == 'POST':
        new_status = request.POST['status']
        table.status = new_status
        table.save()
        return redirect('table_list')
    return render(request, 'templates/change_status.html', {'table': table})

@permission_required('management.seat_plan', raise_exception=True)
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

    return render(request, 'templates/seat_plan.html', context)

# Promotion Management
@permission_required('management.promotion_list', raise_exception=True)
def promotion_list(request):
    promotions = Promotion.objects.filter(is_active=True)
    return render(request, 'templates/promotion_list.html', {'promotions': promotions})

@permission_required('management.promotion_create', raise_exception=True)
def promotion_create(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm()
    return render(request, 'templates/promotion_form.html', {'form': form})

@permission_required('management.promotion_edit', raise_exception=True)
def promotion_edit(request, pk):
    promotion = Promotion.objects.get(pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'templates/promotion_form.html', {'form': form})

@permission_required('management.dish_list', raise_exception=True)
def dish_list(request):
    dishes = Dish.objects.filter(is_available=True)
    return render(request, 'templates/dish_list.html', {'dishes': dishes})

@permission_required('management.dish_create', raise_exception=True)
def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'templates/dish_form.html', {'form': form})

@permission_required('management.dish_edit', raise_exception=True)
def dish_edit(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'templates/dish_form.html', {'form': form})