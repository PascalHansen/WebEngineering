from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from .models import Reservations
from management.models import Notification

#@permission_required('reservations.reservation_list', raise_exception=True)
def reservation_list(request):
    reservations = Reservations.objects.all()
    notifications = Notification.objects.all().order_by('-id')  
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations, 'notifications': notifications})

@permission_required('reservations.add_reservation', raise_exception=True)
def reservation_add(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            message = f"{datetime.now()} - {reservation.guest_name} - added reservation. Table number: {reservation.table.table_number}"
            Notification.objects.create(message=message)
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

@permission_required('reservations.view_reservationdetail', raise_exception=True)
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservations, pk=pk)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

@permission_required('reservations.change_reservation', raise_exception=True)
def reservation_edit(request, pk):
    reservation = Reservations.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save()
            message = f"{datetime.now()} - {reservation.guest_name} - change reservation. New table: {updated_reservation.table.table_number}"
            Notification.objects.create(message=message)
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    
    return render(request, 'reservations/reservation_edit.html', {'form': form, 'reservation': reservation})

@permission_required('reservations.delete_reservation', raise_exception=True)
def reservation_delete(request, pk):
    reservation = Reservations.objects.get(pk=pk)
    message = f"{datetime.now()} - {reservation.guest_name} - deleted reservation for table: {reservation.table.table_number}"
    Notification.objects.create(message=message)
    reservation.delete()
    return redirect('reservation_list')

