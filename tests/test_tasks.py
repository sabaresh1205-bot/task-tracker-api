from django.test import TestCase
from rest_framework.test import APIClient

class TaskTest(TestCase):
    
    def setUp(self):   
        self.client = APIClient()
        self.client.post("/auth/register/", {
            "username": "user1",
            "email": "user@test.com",
            "password": "123456",
            "role": "user"
        })

        login = self.client.post("/auth/login/", {
            "username": "user1",
            "password": "123456"
        })
        
        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        
    def test_create_task(self):

        response = self.client.post("/tasks/", {
            "title": "Test Task",
            "description": "Testing API"
        })

        self.assertEqual(response.status_code, 201)
