# Generated by Django 4.1.4 on 2022-12-11 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_usermodel_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usermodel',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='last_login',
        ),
    ]
