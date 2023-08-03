# Generated by Django 4.2.2 on 2023-07-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0010_alter_sourcetype_st_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='sourcetype',
            name='st_code',
            field=models.CharField(error_messages='Data already existed', max_length=5, unique=True),
        ),
    ]
