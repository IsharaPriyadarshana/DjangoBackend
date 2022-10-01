from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Cart, CartItem
from products.models import Product
from .serializers import CartSerializer, cartItemSerializer
from products.serializers import ProductSerializer
from rest_framework import status
from orders.models import Order
from datetime import datetime


class AddCartItem(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, ordered=False)
        data = request.data
        count = data.get('count')
        productId = data.get('product_id')
        product = Product.objects.get(pk=productId)

        if not cart.exists():
            cart = Cart.objects.create(user=request.user, price= product.price * int(count))
        else:
            cart = cart[0]
            cart.price = cart.price + product.price * int(count)
            cart.save()
        cart_item = CartItem.objects.filter(cart=cart, product=product)
        
        if cart_item.exists():
            cart_item = cart_item[0]
            cart_item.quantity = cart_item.quantity + int(count)
            cart_item.price = cart_item.price + int(count) * product.price 
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(product=product, quantity = int(count), price = product.price * int(count), cart = cart)
        
        return Response({"product" : ProductSerializer(product).data , "cart_item" : cartItemSerializer(cart_item).data, "cart" : CartSerializer(cart).data})


class ViewCartAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user   
        cart = Cart.objects.filter(user=user, ordered=False)
        if not cart.exists():
            return Response({})
        cart = cart[0]
        items = CartItem.objects.filter(cart=cart)
        products = []
        for item in items:
            products.append({"id" : item.id, "item" : item.product.name, "count" : item.quantity, "unit_price" : item.product.price, "price" : item.price})
        return Response({"cart" : products, "total" : cart.price})

class RemoveCartItemAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, id):
        cart = Cart.objects.filter(user=request.user, ordered=False)[0]
        item = CartItem.objects.get(pk=id)
        if(item.cart == cart):
            cart.price = cart.price - (item.price)
            cart.save()
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "invalid request"},status=status.HTTP_400_BAD_REQUEST)


class OrderCartAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        deliver_datetime = request.data.get("deliver_datetime")
        cart = Cart.objects.filter(user=user, ordered=False)
        if not cart.exists():
            return Response({"info" : "No items in the cart"}, status= status.HTTP_400_BAD_REQUEST)
        else:
            cart = cart[0]
            cart.ordered = True
            cart.save()
            dt_obj = datetime.strptime(deliver_datetime, '%d/%m/%y %H:%M')
            order = Order.objects.create(cart=cart, user=user, deliveryDate = dt_obj)
            order.save()
            return Response({"info" : "Order placed"})