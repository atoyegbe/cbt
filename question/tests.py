import json

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from faker import Faker

from pretestrunner import valid_payload
from cbtuser.models import CBTUser
from exam.models import Exam
from question.models import Question

faker = Faker()

class CreateQuestionTest(TestCase):

    def setUp(self) -> None:
        
        self.client = APIClient()
        self.user = User.objects.create_user(username="diaP123", email=valid_payload["email"], password=valid_payload["password"])
        self.user.save()
        self.token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION = "Token " + str(self.token[0]))
        self.cbtuser = CBTUser.objects.create(user=self.user)
        self.cbtuser.save()
        self.exam = Exam.objects.create(title="Computer Science 101", description=faker.text(1400), exam_code="CSC 101")
        self.exam.save()
        self.valid_payload = {
            'description': faker.text(1400),
            'correct_option': "",
        }
        self.invalid_payload = {
            'description': "", #this field cannot be blank
            'correct_option': "",
        }
    
    def test_valid_create_question(self):
        response = self.client.post(
            path = f"/api/v1/question/create/{self.exam.id}",
            data = json.dumps(self.valid_payload),
            content_type = 'application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # check it in the DB
        key = json.loads(response.content).get("id")
        assert Question.objects.get(pk = key) != None

    def test_invalid_create_question(self):
        response = self.client.post(
            path = f"/api/v1/question/create/{self.exam.id}",
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self) -> None:
        return super().tearDown()
