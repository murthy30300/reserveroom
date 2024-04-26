# Generated by Django 5.0.1 on 2024-03-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hoteldetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=255)),
                ('noofrooms', models.IntegerField()),
                ('hoteldesc', models.TextField()),
                ('hotellocation', models.CharField(max_length=255)),
                ('hotelavgroomcostpn', models.IntegerField()),
                ('hotelimage', models.ImageField(blank=True, null=True, upload_to='static/media/hotelimages/')),
            ],
        ),
    ]