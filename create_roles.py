import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reservation.settings')
django.setup()
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from reservations.models import Reservations
from reviews.models import Review
from restaurants.models import Restaurant, Menu, Photo, Booking
from management.models import Table, Promotion, Dish, Notification, SpecialOffer
from users.models import CustomUser

# Erstellen der Gruppen
customer_group, created = Group.objects.get_or_create(name='Customer')
owner_group, created = Group.objects.get_or_create(name='RestaurantManager')
marketing_group, created = Group.objects.get_or_create(name='Marketing')
staff_group, created = Group.objects.get_or_create(name='Staff') # Bisher ungenutzt

# Berechtigungen definieren

# Für Reservierungen
reservations_content_type = ContentType.objects.get_for_model(Reservations, Notification)

can_view_reservationlist, created = Permission.objects.get_or_create(
    codename='reservation_list',
    content_type=reservations_content_type,
)

can_view_reservationdetail, created = Permission.objects.get_or_create(
    codename='view_reservationdetail',
    content_type=reservations_content_type,
)

can_edit_reservation, created = Permission.objects.get_or_create(
    codename='change_reservation',
    content_type=reservations_content_type,
)

can_add_reservation, created = Permission.objects.get_or_create(
    codename='add_reservation',
    content_type=reservations_content_type,
)

can_delete_reservation, created = Permission.objects.get_or_create(
    codename='delete_reservation',
    content_type=reservations_content_type,
)

# Für Reviews
review_content_type = ContentType.objects.get_for_model(Review)

can_add_review, created = Permission.objects.get_or_create(
    codename='add_review',
    content_type=review_content_type,
)

can_delete_review, created = Permission.objects.get_or_create(
    codename='delete_review',
    content_type=review_content_type,
)

# Für Restaurant Management
restaurant_content_type = ContentType.objects.get_for_model(Restaurant, Menu)
restaurant_content_type = ContentType.objects.get_for_model(Photo, Booking)

owner_dashboard, created = Permission.objects.get_or_create(
    codename='owner_dashboard',
    content_type=restaurant_content_type,
)

can_create_restaurant, created = Permission.objects.get_or_create(
    codename='create_restaurant',
    content_type=restaurant_content_type,
)

can_update_restaurant, created = Permission.objects.get_or_create(
    codename='update_restaurant',
    content_type=restaurant_content_type,
)

can_update_menu, created = Permission.objects.get_or_create(
    codename='update_menu',
    content_type=restaurant_content_type,
)

can_update_photo, created = Permission.objects.get_or_create(
    codename='update_photo',
    content_type=restaurant_content_type,
)

can_delete_restaurant, created = Permission.objects.get_or_create(
    codename='delete_restaurant',
    content_type=restaurant_content_type,
)

customer_data, created = Permission.objects.get_or_create(
    codename='customer_data',
    content_type=restaurant_content_type,
)

trend_analysis, created = Permission.objects.get_or_create(
    codename='trend_analysis',
    content_type=restaurant_content_type,
)

can_generate_report, created = Permission.objects.get_or_create(
    codename='generate_report',
    content_type=restaurant_content_type,
)

# Management (Tische und Notifications, + Marketing)
management_content_type = ContentType.objects.get_for_model(Table, Promotion)
management_content_type = ContentType.objects.get_for_model(Dish, Notification)
management_content_type = ContentType.objects.get_for_model(SpecialOffer)

table_list, created = Permission.objects.get_or_create(
    codename='table_list',
    content_type=management_content_type,
)

can_change_status, created = Permission.objects.get_or_create(
    codename='change_status',
    content_type=management_content_type,
)

seat_plan, created = Permission.objects.get_or_create(
    codename='seat_plan',
    content_type=management_content_type,
)

can_promotion_create, created = Permission.objects.get_or_create(
    codename='promotion_create',
    content_type=management_content_type,
)

can_promotion_edit, created = Permission.objects.get_or_create(
    codename='promotion_edit',
    content_type=management_content_type,
)

can_dish_create, created = Permission.objects.get_or_create(
    codename='dish_create',
    content_type=management_content_type,
)

can_dish_edit, created = Permission.objects.get_or_create(
    codename='dish_edit',
    content_type=management_content_type,
)

can_get_notifications, created = Permission.objects.get_or_create(
    codename='get_notifications',
    content_type=management_content_type,
)

can_clear_notifications, created = Permission.objects.get_or_create(
    codename='clear_notifications',
    content_type=management_content_type,
)

can_create_specialoffer, created = Permission.objects.get_or_create(
    codename='special_offer',
    content_type=management_content_type,
)

# Für User
users_content_type = ContentType.objects.get_for_model(CustomUser)

can_view_profile, created = Permission.objects.get_or_create(
    codename='profile_view',
    content_type=users_content_type,
)

# Berechtigungen zu Gruppen hinzufügen
customer_group.permissions.add(can_view_reservationlist, can_view_reservationdetail, can_add_reservation, can_add_review, can_delete_review, can_view_profile)
owner_group.permissions.add(can_view_reservationlist, can_view_reservationdetail, can_edit_reservation, can_delete_reservation, owner_dashboard, can_create_restaurant, 
                            can_update_restaurant, can_update_menu, can_update_photo, can_delete_restaurant, can_get_notifications, can_change_status, seat_plan, 
                            can_promotion_create, can_promotion_edit, can_dish_create, can_dish_edit, can_clear_notifications, can_view_profile)
marketing_group.permissions.add(customer_data, trend_analysis, can_generate_report)
staff_group.permissions.add()

customer_group.save()
owner_group.save()
marketing_group.save()
staff_group.save()

print("Gruppen und Berechtigungen wurden erfolgreich erstellt und zugewiesen.")