# Generated by Django 5.0.6 on 2024-06-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion_management', '0003_dish_delete_loyaltyprogram_promotion_points_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='points_required',
            new_name='loyalty_points_required',
        ),
        migrations.RenameField(
            model_name='promotion',
            old_name='points',
            new_name='loyalty_points',
        ),
        migrations.RenameField(
            model_name='promotion',
            old_name='special_item',
            new_name='special_menu_item',
        ),
        migrations.AddField(
            model_name='dish',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Verfügbar'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Gerichtname'),
        ),
    ]
