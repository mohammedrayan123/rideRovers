# Generated by Django 4.2.7 on 2024-02-01 10:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mvrr', '0014_bikedata_bookedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikedata',
            name='bookedat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 37, 25, 564037)),
        ),
        migrations.CreateModel(
            name='BookingData',
            fields=[
                ('bookingid', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('onrname', models.CharField(max_length=50)),
                ('regno', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('bikename', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('chassis_no', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('dop', models.DateField(blank=True, null=True)),
                ('bikepic', models.ImageField(upload_to='bike_uploads/')),
                ('biketype', models.CharField(choices=[('CLASSIC', 'Classic'), ('STREET BIKE', 'Street Bike'), ('COMMUTER', 'Commuter'), ('SPORTS BIKE', 'Sports Bike'), ('CHAPRI BIKE', 'Chapri Bike')], default='CLASSIC', max_length=20)),
                ('bookedat', models.DateTimeField(default=datetime.datetime(2024, 2, 1, 15, 37, 25, 564037))),
                ('pickup_date', models.DateField()),
                ('pickup_time', models.TimeField()),
                ('dropoff_date', models.DateField()),
                ('dropoff_time', models.TimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvrr.bikedata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
