# Generated by Django 4.2.2 on 2023-07-27 03:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ad", "0007_customuser"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
