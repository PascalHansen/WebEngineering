from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import Reservations
from reservations.forms import ReservationForm
from .models import Notification

def notification_list(request):
    notifications = Notification.objects.all().order_by('-timestamp')
    return render(request, 'templates/notification_list.html', {'notifications': notifications})


# Warum sind hier Reservation nochmal neu aufgebaut?
def reservation_list(request):
    reservations = Reservations.objects.all()
    return render(request, 'reservation_management/reservation_list.html', {'reservations': reservations})

def reservation_add(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation_management/reservation_form.html', {'form': form})

def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservations, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation_management/reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservations, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservation_management/reservation_confirm_delete.html', {'reservation': reservation})

def clear_notifications(request):
    if request.method == 'POST':
        Notification.objects.all().delete()
    
    return redirect('notification_list')