# Generated by Django 4.1.4 on 2022-12-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_usermodel_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='ex',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
