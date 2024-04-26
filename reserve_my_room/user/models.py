import datetime

from django.db import models


class room_details(models.Model):
    name = models.CharField(max_length=20, blank=True,default="abc" )
    email = models.EmailField(max_length=20, default='22@gmail.com' )
    phone = models.BigIntegerField(max_length=10, default='9999' )
    check_in = models.DateField(max_length=10 )
    check_out = models.DateField(max_length=10 )
    city = models.CharField(max_length=10,default='huh' )
    country = models.CharField(max_length=10,default='india' )
    adults = models.IntegerField(max_length=2, default='1' )
    children = models.IntegerField(max_length=2,default=1 )
    address = models.TextField(max_length=200,default='aaaaaa' )

    def __str__(self):
        return self.name
