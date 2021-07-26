import json

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from cbtuser.views import generate_username


client = Client(enforce_csrf_checks=False) # in testmode this is False


class CreateCBTUserTest(TestCase):
    """ Test module for create CBTUser API """

    def setUp(self):
        self.valid_payload = {
            'date_of_birth': '1948-11-29',
            'first_name': "Dianna",
            'last_name': 'Pamerion',
            'password': 'password123',
            'email': 'dianna@cbt.com'
        }
        self.invalid_payload = {
            'date_of_birth': '',
            'first_name': "Mai",
            'email': 'ema#mail.com'
        }


    def test_generate_username(self):
        self.assertTrue(type(generate_username("adele loaves")) == str) 
        self.assertTrue(len(generate_username("Matt Ha"))> 1)
        try:
            generate_username()
        except ValueError:
            pass
        finally:
            self.assertTrue(True,True)

    def test_create_valid_cbtuser(self):
        response = client.post(
            path = reverse('create_cbtuser'),
            data = json.dumps(self.valid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_invalid_cbtuser(self):
        response = client.post(
            path  = reverse('create_cbtuser'),
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

class LoginCBTUserTest(TestCase):
        
    def setUp(self) -> None:
        self.user = User.objects.create_user(username = "abc123", 
                                            password= "password123", 
                                            email="dianna@cbt.com")
        self.user.save()
        
        self.valid_payload = {
            'username': self.user.username,
            'password': 'password123',
        }
        self.invalid_payload_password = {
            'username': self.user.username,
            'password': 'pas123',
        }
        self.invalid_payload = {
            'username': self.user.username,
        }

    def test_valid_login_cbtuser(self):
        response = client.post(
            path = reverse('login_cbtuser'),
            data = json.dumps(self.valid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_login_cbtuser(self):
        response = client.post(
            path = reverse('login_cbtuser'),
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = client.post(
            path = reverse('login_cbtuser'),
            data = json.dumps(self.invalid_payload_password),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)