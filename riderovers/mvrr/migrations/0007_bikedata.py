# Generated by Django 4.2.7 on 2024-01-29 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mvrr', '0006_kycdata_delete_kyc'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeData',
            fields=[
                ('bikeid', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('onrname', models.CharField(max_length=50)),
                ('regno', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('bikename', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('chessis_no', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('dop', models.DateField(blank=True, null=True)),
                ('bikepic', models.ImageField(upload_to='bike_uploads/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]