# Generated by Django 4.2.7 on 2024-01-29 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvrr', '0009_merge_20240129_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikeimage',
            name='bike',
        ),
        migrations.DeleteModel(
            name='Bike',
        ),
        migrations.DeleteModel(
            name='BikeImage',
        ),
    ]
