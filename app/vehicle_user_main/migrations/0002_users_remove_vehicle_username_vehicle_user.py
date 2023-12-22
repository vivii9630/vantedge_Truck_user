# Generated by Django 5.0 on 2023-12-22 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_user_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='username',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(default='SOME STRING', on_delete=django.db.models.deletion.CASCADE, to='vehicle_user_main.users'),
        ),
    ]
