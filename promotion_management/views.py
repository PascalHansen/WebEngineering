

from django.shortcuts import render, redirect
from .models import Promotion, Dish
from .forms import PromotionForm, DishForm

def promotion_list(request):
    promotions = Promotion.objects.filter(is_active=True)
    return render(request, 'promotion_management/promotion_list.html', {'promotions': promotions})

def promotion_create(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm()
    return render(request, 'promotion_management/promotion_form.html', {'form': form})

def promotion_edit(request, pk):
    promotion = Promotion.objects.get(pk=pk)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect('promotion_list')
    else:
        form = PromotionForm(instance=promotion)
    return render(request, 'promotion_management/promotion_form.html', {'form': form})

def dish_list(request):
    dishes = Dish.objects.filter(is_available=True)
    return render(request, 'promotion_management/dish_list.html', {'dishes': dishes})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'promotion_management/dish_form.html', {'form': form})

def dish_edit(request, pk):
    dish = Dish.objects.get(pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'promotion_management/dish_form.html', {'form': form})
