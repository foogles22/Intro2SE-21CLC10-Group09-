# Generated by Django 4.2.2 on 2023-08-07 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0012_alter_loantransaction_date_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_blog',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='loantransaction',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2023, 8, 14, 15, 55, 4, 823231, tzinfo=datetime.timezone.utc)),
        ),
    ]
