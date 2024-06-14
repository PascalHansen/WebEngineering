from django.shortcuts import render, redirect
from .models import Table
from reservation_management.models import Reservation


def table_list(request):
    tables = Table.objects.all().order_by('table_number')
    return render(request, 'table_seating_management/table_list.html', {'tables': tables})

def change_status(request, table_id):
    table = Table.objects.get(pk=table_id)
    if request.method == 'POST':
        new_status = request.POST['status']
        table.status = new_status
        table.save()
        return redirect('table_list')
    return render(request, 'table_seating_management/change_status.html', {'table': table})

def seat_plan(request):
    tables_with_guests = {}

    tables = Table.objects.all()

    for table in tables:
        tables_with_guests[table] = []

    reservations = Reservation.objects.all()

    for reservation in reservations:
        if reservation.table in tables_with_guests:
            tables_with_guests[reservation.table].append(reservation)

    context = {
        'tables_with_guests': tables_with_guests,
    }

    return render(request, 'table_seating_management/seat_plan.html', context)