# Generated by Django 5.0.1 on 2024-04-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_userprofile_address_remove_userprofile_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.BigIntegerField(max_length=10)),
                ('check_in', models.DateField(max_length=10)),
                ('check_out', models.DateField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('adults', models.IntegerField(max_length=2)),
                ('children', models.IntegerField(max_length=2)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='hoteldetails',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]