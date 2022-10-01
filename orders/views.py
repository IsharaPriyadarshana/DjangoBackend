from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Order
from cart.models import Cart, CartItem
from products.models import Product
from accounts.serializers import UserSerializer
from rest_framework import status


class OrdersAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self,request):
        orders = Order.objects.all()
        data = []
        for order in orders:
            items = CartItem.objects.filter(cart=order.cart)
            products = []
            for item in items:
                products.append({"id" : item.id, "item" : item.product.name, "count" : item.quantity, "unit_price" : item.product.price, "price" : item.price})
            data.append({"user" : UserSerializer(order.user).data, "delivery-date" : order.deliveryDate, "cart" : {"total" : order.cart.price, "items" : products}})
        return Response({"orders" : data})


# # Create your views here.
# def order(request : HttpRequest):
#     cart = Cart.objects.filter(user = request.user, ordered=False)[0]
#     cart.ordered = True
#     cart.save()
#     deliveryDate = request.POST.get('orderDate')
#     if deliveryDate == "":
#         deliveryDate = datetime.now()
#     Order.objects.create(user=request.user, cart = cart, deliveryDate = deliveryDate)
#     return redirect("/")