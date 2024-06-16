# Generated by Django 5.0.6 on 2024-06-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('restaurant_manager', 'Restaurant Manager'), ('marketing', 'Marketing'), ('staff', 'Staff')], default='customer', max_length=20),
        ),
    ]