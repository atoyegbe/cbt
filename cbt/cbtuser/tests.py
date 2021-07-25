import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from cbtuser.views import generate_username

client = Client()


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