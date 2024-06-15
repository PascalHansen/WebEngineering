# Generated by Django 5.0.6 on 2024-06-15 12:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Gerichtname')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('loyalty_points_required', models.IntegerField(verbose_name='Erforderliche Treuepunkte')),
                ('is_available', models.BooleanField(default=True, verbose_name='Verfügbar')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('description', models.TextField(verbose_name='Beschreibung')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Rabatt')),
                ('special_menu_item', models.CharField(blank=True, max_length=100, null=True, verbose_name='Spezialmenüartikel')),
                ('loyalty_points', models.IntegerField(default=0, verbose_name='Treuepunkte')),
                ('start_date', models.DateField(verbose_name='Startdatum')),
                ('end_date', models.DateField(verbose_name='Enddatum')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('status', models.CharField(choices=[('Frei', 'Frei'), ('Reserviert', 'Reserviert'), ('Außer Betrieb', 'Außer Betrieb')], max_length=15)),
            ],
        ),
    ]