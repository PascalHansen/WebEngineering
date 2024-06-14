

from django.shortcuts import render, redirect
from notifications_management.models import Notification
from .forms import ReservationForm
from datetime import datetime
from reservation_management.models import Reservation


def reservation_list(request):
    reservations = Reservation.objects.all()
    notifications = Notification.objects.all().order_by('-id')  
    return render(request, 'reservation_management/reservation_list.html', {'reservations': reservations, 'notifications': notifications})

def reservation_add(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            message = f"{datetime.now()} - {reservation.guest_name} - Reservierung hinzugefügt. Tischnummer: {reservation.table.table_number}"
            Notification.objects.create(message=message)
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation_management/reservation_form.html', {'form': form})

def reservation_edit(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save()
            message = f"{datetime.now()} - {reservation.guest_name} - Reservierung geändert. Neue Tischnummer: {updated_reservation.table.table_number}"
            Notification.objects.create(message=message)
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    
    return render(request, 'reservation_management/reservation_edit.html', {'form': form, 'reservation': reservation})

def reservation_delete(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    message = f"{datetime.now()} - {reservation.guest_name} - Reservierung gelöscht. Tischnummer: {reservation.table.table_number}"
    Notification.objects.create(message=message)
    reservation.delete()
    return redirect('reservation_list')
