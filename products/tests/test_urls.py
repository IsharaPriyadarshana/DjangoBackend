import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import products, detail

class TestUrls(SimpleTestCase):

    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, products)
    
    def test_detail_url_is_resolved(self):
        url = reverse('detail')
        self.assertEquals(resolve(url).func, detail)