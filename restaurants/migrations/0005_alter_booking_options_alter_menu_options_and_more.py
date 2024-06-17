# Generated by Django 5.0.6 on 2024-06-16 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_alter_photo_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'permissions': [('customer_data', 'Can access customer data'), ('trend_analysis', 'Can access the trend analysis'), ('generate_report', 'Can generate reports')]},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'permissions': [('update_menu', 'Can update the menu')]},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'permissions': [('update_photo', 'Can update the photo')]},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'permissions': [('owner_dashboard', 'Can access the owner dashboard'), ('create_restaurant', 'Can add restaurants'), ('update_restaurant', 'Can update restaurants')]},
        ),
    ]
