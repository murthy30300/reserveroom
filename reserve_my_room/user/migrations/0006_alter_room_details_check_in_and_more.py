# Generated by Django 5.0.1 on 2024-04-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_room_details_address_alter_room_details_adults_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_details',
            name='check_in',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='room_details',
            name='check_out',
            field=models.DateField(max_length=10),
        ),
    ]
