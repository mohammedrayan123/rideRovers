# Generated by Django 4.2.7 on 2024-02-04 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvrr', '0019_alter_bikedata_bookedat_alter_bookingdata_bookedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikedata',
            name='bookedat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 0, 22, 59, 990556)),
        ),
        migrations.AlterField(
            model_name='bookingdata',
            name='bookedat',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 0, 22, 59, 990556)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_host',
            field=models.IntegerField(default=0),
        ),
    ]