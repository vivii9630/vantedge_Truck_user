# Generated by Django 5.0 on 2023-12-22 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_user_main', '0005_rename_user_vehicle_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='username',
            new_name='user',
        ),
    ]
