from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    longDesc = models.TextField(default="This contains a detailed description of the product")
    price = models.FloatField()