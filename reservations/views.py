from django.shortcuts import render, redirect
from .forms import ReservationForm

def book_reservation(request, restaurant_id):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.restaurant_id = restaurant_id
            reservation.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/book_reservation.html', {'form': form})