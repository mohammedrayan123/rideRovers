# Generated by Django 4.2.7 on 2024-01-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvrr', '0003_remove_userprofile_id_userprofile_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_host',
            field=models.BooleanField(default=False),
        ),
    ]
