# Generated by Django 4.2.2 on 2023-08-07 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0005_remove_comment_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransaction',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2023, 8, 14, 7, 46, 20, 214486, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/'),
        ),
    ]
