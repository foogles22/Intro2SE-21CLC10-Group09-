# Generated by Django 4.2.2 on 2023-08-07 08:04

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0008_profile_bio_alter_loantransaction_date_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='loantransaction',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2023, 8, 14, 8, 4, 32, 73219, tzinfo=datetime.timezone.utc)),
        ),
    ]
