# Generated by Django 4.2.7 on 2024-01-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvrr', '0011_bikedata_biketype'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikedata',
            name='id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]