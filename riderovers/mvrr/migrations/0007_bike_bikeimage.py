# Generated by Django 4.2.7 on 2024-01-29 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mvrr', '0006_kycdata_delete_kyc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=20, unique=True)),
                ('company', models.CharField(max_length=255)),
                ('bike_name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=50)),
                ('chassis_no', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_of_purchase', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BikeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bike_images/')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvrr.bike')),
            ],
        ),
    ]
