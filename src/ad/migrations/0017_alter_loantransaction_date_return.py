# Generated by Django 4.2.2 on 2023-07-29 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ad", "0016_loantransaction_returned_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loantransaction",
            name="date_return",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 5, 3, 19, 8, 135515, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
