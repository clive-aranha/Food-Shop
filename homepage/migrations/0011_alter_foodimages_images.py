# Generated by Django 5.0.7 on 2024-09-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_alter_foodimages_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodimages',
            name='images',
            field=models.ImageField(upload_to='foodimages/'),
        ),
    ]