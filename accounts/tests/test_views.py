from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        user = User.objects.create_user(username='user', password='1234', email='user@autocompany.com', first_name = 'Tom', last_name='Riddle')
        user.save()

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_POST(self):
        response = self.client.post(self.register_url, 
        {'first_name' : 'Arya', 
        'last_name' : 'Stark',
        'user_name' : 'a_stark',
        'password1' : 'theNorthRemembers',
        'password2' : 'theNorthRemembers',
        'email' : 'arya@autocompany.com'})
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(len(User.objects.filter(username='a_stark')), 1)

    def test_logout_GET(self):
        self.client.login(username="user", password="1234")
        response = self.client.get(self.logout_url)
        
        self.assertEquals(response.status_code, 302)
        self.assertNotEqual(response.wsgi_request.user, 'user')
    
    def test_login_GET(self):
        response = self.client.get(self.login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    # def test_login_POST(self):
    #     response = self.client.post(reverse("login"), {
    #         'username' : 'user',
    #         'password' : '1234'
    #     })
        
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'login.html')
    
    

