# Generated by Django 5.0.7 on 2024-09-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_foodimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodimages',
            name='images',
            field=models.ImageField(upload_to='Foodimages/'),
        ),
    ]