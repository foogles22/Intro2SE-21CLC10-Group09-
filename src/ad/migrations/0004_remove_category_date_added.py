# Generated by Django 4.2.2 on 2023-06-19 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0003_category_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='date_added',
        ),
    ]
