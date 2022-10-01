from itertools import product
from statistics import quantiles
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart, CartItem

# Create your models here.
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deliveryDate = models.DateTimeField(null=True)