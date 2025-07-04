# Generated by Django 5.2.3 on 2025-06-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_deals_alter_menu_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('c_phone', models.CharField(max_length=10)),
                ('c_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('no_guest', models.CharField(max_length=255)),
                ('seating_pref', models.CharField()),
                ('sp_request', models.TextField()),
                ('booked_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
