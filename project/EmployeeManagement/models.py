from django.db import models


# Create your models here.
class cart(models.Model):
    name=models.CharField(max_length=255)  
    brand=models.CharField(max_length=255)
    size=models.IntegerField()
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    