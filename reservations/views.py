from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from .models import Reservations
from notifications.models import Notification

@permission_required('reservations.view_reservation', raise_exception=True)
def reservation_list(request):
    reservations = Reservations.objects.all()
    notifications = Notification.objects.all().order_by('-id')  
    return render(request, 'templates/reservation_list.html', {'reservations': reservations, 'notifications': notifications})

@permission_required('reservations.add_reservation', raise_exception=True)
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

@permission_required('reservations.change_reservation', raise_exception=True)
def reservation_edit(request, pk):
    reservation = Reservations.objects.get(pk=pk)
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

@permission_required('reservations.delete_reservation', raise_exception=True)
def reservation_delete(request, pk):
    reservation = Reservations.objects.get(pk=pk)
    message = f"{datetime.now()} - {reservation.guest_name} - Reservierung gelöscht. Tischnummer: {reservation.table.table_number}"
    Notification.objects.create(message=message)
    reservation.delete()
    return redirect('reservation_list')

