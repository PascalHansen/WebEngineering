from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from reservations.models import Reservations
from reviews.models import Review
from restaurants.models import Restaurant, Menu, Photo, Booking
from management.models import Table, Promotion, Dish, Notification

# Erstellen der Gruppen
customer_group, created = Group.objects.get_or_create(name='Customer')
owner_group, created = Group.objects.get_or_create(name='RestaurantManager')
marketing_group, created = Group.objects.get_or_create(name='Marketing')
staff_group, created = Group.objects.get_or_create(name='Staff') # Bisher ungenutzt

# Berechtigungen definieren

# Für Reservierungen
reservations_content_type = ContentType.objects.get_for_model(Reservations)

can_view_reservationlist = Permission.objects.get(
    codename='view_reservationlist',
    content_type=reservations_content_type,
)

can_view_reservationdetail = Permission.objects.get(
    codename='view_reservationdetail',
    content_type=reservations_content_type,
)

can_edit_reservation = Permission.objects.get(
    codename='change_reservation',
    content_type=reservations_content_type,
)

can_add_reservation = Permission.objects.get(
    codename='add_reservation',
    content_type=reservations_content_type,
)

can_delete_reservation = Permission.objects.get(
    codename='delete_reservation',
    content_type=reservations_content_type,
)

# Für Reviews
review_content_type = ContentType.objects.get_for_model(Review)

can_add_review = Permission.objects.get(
    codename='add_review',
    content_type=review_content_type,
)

can_delete_review = Permission.objects.get(
    codename='delete_review',
    content_type=review_content_type,
)

# Für Restaurant Management
restaurant_content_type = ContentType.objects.get_for_model(Restaurant, Menu, Photo, Booking)

owner_dashboard = Permission.objects.get(
    codename='owner_dashboard',
    content_type=restaurant_content_type,
)

can_create_restaurant = Permission.objects.get(
    codename='create_restaurant',
    content_type=restaurant_content_type,
)

can_update_restaurant = Permission.objects.get(
    codename='update_restaurant',
    content_type=restaurant_content_type,
)

can_update_menu = Permission.objects.get(
    codename='update_menu',
    content_type=restaurant_content_type,
)

can_update_photo = Permission.objects.get(
    codename='update_photo',
    content_type=restaurant_content_type,
)

can_delete_restaurant = Permission.objects.get(
    codename='delete_restaurant',
    content_type=restaurant_content_type,
)

customer_data = Permission.objects.get(
    codename='customer_data',
    content_type=restaurant_content_type,
)

trend_analysis = Permission.objects.get(
    codename='trend_analysis',
    content_type=restaurant_content_type,
)

can_generate_report = Permission.objects.get(
    codename='generate_report',
    content_type=restaurant_content_type,
)

# Management (Tische und Notifications)
management_content_type = ContentType.objects.get_for_model(Table, Promotion, Dish, Notification)
# Florian morgen noch Fragen, wer welche Berechtigungen braucht
table_list = Permission.objects.get(
    codename='table_list',
    content_type=management_content_type,
)

can_change_status = Permission.objects.get(
    codename='change_status',
    content_type=management_content_type,
)

seat_plan = Permission.objects.get(
    codename='seat_plan',
    content_type=management_content_type,
)

promotion_list = Permission.objects.get(
    codename='promotion_list',
    content_type=management_content_type,
)

can_promotion_create = Permission.objects.get(
    codename='promotion_create',
    content_type=management_content_type,
)

can_promotion_edit = Permission.objects.get(
    codename='promotion_edit',
    content_type=management_content_type,
)

dish_list = Permission.objects.get(
    codename='dish_list',
    content_type=management_content_type,
)

can_dish_create = Permission.objects.get(
    codename='dish_create',
    content_type=management_content_type,
)

can_dish_edit = Permission.objects.get(
    codename='dish_edit',
    content_type=management_content_type,
)

can_get_notifications = Permission.objects.get(
    codename='get_notifications',
    content_type=management_content_type,
)

can_clear_notifications = Permission.objects.get(
    codename='clear_notifications',
    content_type=management_content_type,
)

can_access_edit = Permission.objects.get(
    codename='access_edit',
    content_type=management_content_type,
)
# Berechtigungen zu Gruppen hinzufügen
customer_group.permissions.add(can_view_reservationlist, can_view_reservationdetail, can_add_reservation, can_add_review, can_delete_review)
owner_group.permissions.add(can_view_reservationlist, can_view_reservationdetail, can_edit_reservation, can_delete_reservation, owner_dashboard, can_create_restaurant, 
                            can_update_restaurant, can_update_menu, can_update_photo, can_delete_restaurant, can_get_notifications, can_change_status, seat_plan, 
                            promotion_list, can_promotion_create, can_promotion_edit, dish_list, can_dish_create, can_dish_edit, can_clear_notifications, can_access_edit)
marketing_group.permissions.add(customer_data, trend_analysis, can_generate_report)
staff_group.permissions.add()

print("Gruppen und Berechtigungen wurden erfolgreich erstellt und zugewiesen.")