from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import add, remove, view, remove

class TestUrls(SimpleTestCase):

    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func, add)
    
    def test_view_url_is_resolved(self):
        url = reverse('view')
        self.assertEquals(resolve(url).func, view)

    def test_remove_url_is_resolved(self):
        url = reverse('remove')
        self.assertEquals(resolve(url).func, remove)
