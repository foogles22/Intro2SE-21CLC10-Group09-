# Generated by Django 4.2.2 on 2023-07-29 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ad", "0020_remove_loantransaction_date_return_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loantransaction",
            name="date_expired",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 5, 17, 40, 23, 194310, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="loantransaction",
            name="returned",
            field=models.CharField(
                choices=[("0", "No"), ("1", "Yes")], default=0, max_length=2
            ),
        ),
    ]
