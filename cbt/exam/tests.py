from rest_framework.test import APIClient
from faker import Faker

fake = Faker()
client = APIClient()
valid_payload = {
    'title': fake.text(450),
    'description': fake.text(1400),
}