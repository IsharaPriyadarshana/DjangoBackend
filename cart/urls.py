from django.urls import path
from . import views

urlpatterns = [
    path("add", views.AddCartItem.as_view(), name="add"),
    path("", views.ViewCartAPI.as_view(), name="view"),
    path("remove/<int:id>", views.RemoveCartItemAPI.as_view(), name="remove"),
    path('order', views.OrderCartAPI.as_view(), name="order")
]