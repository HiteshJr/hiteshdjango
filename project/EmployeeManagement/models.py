from django.db import models

# Create your models here.

class cart(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size  = models.IntegerField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cart = models.CharField(max_length=100,default='[]')
    address  = models.CharField(max_length=500)
    orderhistory = models.CharField(max_length=1000,default='[]')
