# Generated by Django 4.0.5 on 2022-06-27 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driversapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.DeleteModel(
            name='StationStop',
        ),
    ]
