# Generated by Django 4.2.2 on 2023-08-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0017_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='sourcetype',
            name='st_code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
