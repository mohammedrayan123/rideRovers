# Generated by Django 4.2.7 on 2024-01-31 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mvrr', '0012_bikedata_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikedata',
            name='id',
        ),
    ]
