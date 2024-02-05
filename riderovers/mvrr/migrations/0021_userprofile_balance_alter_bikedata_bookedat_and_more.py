# Generated by Django 4.2.7 on 2024-02-05 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvrr', '0020_alter_bikedata_bookedat_alter_bookingdata_bookedat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bikedata',
            name='bookedat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 23, 40, 37, 512729)),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='bookedat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 23, 40, 37, 512729)),
        ),
    ]
