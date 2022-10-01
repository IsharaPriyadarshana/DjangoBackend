from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status


class addProductAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Product = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class getProductsAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = self.get_serializer(products, many=True)
        # serializer.is_valid(raise_exception=True)
        return Response({"products": serializer.data})


class getDetailsAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer

    def get(self, request, id):
        product = Product.objects.filter(id=id)
        if not product.exists():
            return Response({"error" : "Product with the given ID not found"})
        else:
            product = product[0]
        serializer = self.get_serializer(product)
        # serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

