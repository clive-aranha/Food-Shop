# Generated by Django 5.0.7 on 2024-09-09 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_login_cost_remove_login_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Loginform',
        ),
    ]