from cbtuser.models import CBTUser
import json

from faker import Faker
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from pretestrunner import valid_payload
from exam.models import Exam

faker = Faker()

class CreateExamTest(APITestCase):

    def setUp(self) -> None:
        
        self.valid_payload = {
            "title" : "Computer Science 101",
            "description" : faker.text(1400),
            "exam_code" : "CSC 101"            
        }
        self.invalid_payload = {"title" : "Artificial Neural Network"}
        self.client = APIClient()
        self.user = User.objects.create_user(username="diaP123", email=valid_payload["email"], password=valid_payload["password"])
        self.user.save()
        self.token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + str(self.token[0]))
        self.cbtuser = CBTUser.objects.create(user=self.user)
        self.cbtuser.save()

        
    def test_valid_create_exam(self) -> None:
        response = self.client.post(
            path = reverse('create_exam'),
            data = json.dumps(self.valid_payload),
            content_type = 'application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_invalid_create_exam(self) -> None:
        response = self.client.post(
            path = reverse('create_exam'),
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def tearDown(self) -> None:
        self.user.delete()
        self.cbtuser.delete()


class ReadExamTest(APITestCase):

    def setUp(self) -> None:
        
        self.title = "Art and Science 401"
        self.exam_code = "AS 401"
        self.description = faker.text(1400)
        
        self.client = APIClient()
        self.exam = Exam.objects.create(title=self.title, description=self.description, exam_code= self.exam_code)
        self.exam.save()
        
    def test_valid_read_exam(self) -> None:
        response = self.client.get(path = f"/api/v1/exam/read/{str(self.exam.id)}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_read_exam(self) -> None:
        response = self.client.get(path = f"/api/v1/exam/read/{str(__import__('uuid').uuid4())}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def tearDown(self) -> None:
        self.exam.delete()
