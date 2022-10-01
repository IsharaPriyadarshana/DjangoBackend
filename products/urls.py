from django.urls import path
from . import views

urlpatterns = [
    path("add", views.addProductAPI.as_view(), name="addProduct"),
    path('',views.getProductsAPI.as_view(),name="getProducts" ),
    path("<int:id>", views.getDetailsAPI.as_view(), name="detail"),
]