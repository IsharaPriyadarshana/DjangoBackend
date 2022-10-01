from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrdersAPI.as_view(), name="order")

]