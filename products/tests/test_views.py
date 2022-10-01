from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse("products")
        self.detail_url = reverse("detail")
        user = User.objects.create_user(username='user', password='1234', email='user@autocompany.com', first_name = 'Tom', last_name='Riddle')
        self.product = Product.objects.create(name="Tyres", img="pics/tyres.jpg", desc="Short desc ", longDesc = "Long Desc", price=100)


    def test_products_GET(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(self.products_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')
    

    def test_detail_GET(self):
        response = self.client.get(self.detail_url, {'product' : 'Tyres'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

