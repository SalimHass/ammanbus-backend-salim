# Generated by Django 4.0.5 on 2022-06-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_busstationstop_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stationstop',
            options={'ordering': ['order_number']},
        ),
        migrations.AlterField(
            model_name='stationstop',
            name='time_to_next_station',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='stationstop',
            unique_together={('route', 'station')},
        ),
    ]
