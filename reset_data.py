from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from products.models import Product
from orders.models import Order

Order.objects.all().delete()
CartItem.objects.all().delete()
Product.objects.all().delete()
Cart.objects.all().delete()
User.objects.all().delete()