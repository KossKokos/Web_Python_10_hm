# Generated by Django 4.2.7 on 2023-11-06 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='qoute',
            new_name='quote',
        ),
    ]
