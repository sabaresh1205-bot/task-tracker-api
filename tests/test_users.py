from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class UserAuthTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        
    def test_register_user(self):
        
        data = {
            "username": "testuser",
            "email": "test@test.com",
            "password": "123456",
            "role": "user"
        }
        
        response = self.client.post("/auth/register/", data)
        
        self.assertEqual(response.status_code, 201)
        
    def test_login_user(self):

        self.client.post("/auth/register/", {
        "username": "testuser",
        "email": "test@test.com",
        "password": "123456",
        "role": "user"
        })

        response = self.client.post("/auth/login/", {
        "username": "testuser",
        "password": "123456"
        })

        self.assertEqual(response.status_code, 200)