from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from reservations.models import Reservation

# Gruppen erstellen
customer_group, created = Group.objects.get_or_create(name='Customer')
owner_group, created = Group.objects.get_or_create(name='RestaurantOwner')
staff_group, created = Group.objects.get_or_create(name='Staff')

# Berechtigungen zuweisen
reservation_content_type = ContentType.objects.get_for_model(Reservation)

can_view_reservation = Permission.objects.get(
    codename='view_reservation',
    content_type=reservation_content_type,
)
can_edit_reservation = Permission.objects.get(
    codename='change_reservation',
    content_type=reservation_content_type,
)
can_add_reservation = Permission.objects.get(
    codename='add_reservation',
    content_type=reservation_content_type,
)
can_delete_reservation = Permission.objects.get(
    codename='delete_reservation',
    content_type=reservation_content_type,
)

# Berechtigungen zu Gruppen hinzufügen
customer_group.permissions.add(can_view_reservation, can_add_reservation)
owner_group.permissions.add(can_view_reservation, can_edit_reservation, can_delete_reservation)
staff_group.permissions.add(can_view_reservation, can_edit_reservation)