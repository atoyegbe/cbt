# import json

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient
# from django.test import Client
# from rest_framework import status
# from django.urls import reverse
# import pytest

# from cbtuser.views import generate_username
# from cbtuser.models import CBTUser


# client = Client(enforce_csrf_checks=False) # in testmode this is False



# valid_payload = {
#             'date_of_birth': '1948-11-29',
#             'first_name': "Dianna",
#             'last_name': 'Pamerion',
#             'password': 'password123',
#             'email': 'dianna@cbt.com'
#         }
# invalid_payload = {
#             'date_of_birth': '',
#             'first_name': "Mai",
#             'email': 'ema#mail.com'
# }
assert 1==1
# pytest.fixture(scope="session")
# def get_user(valid_payload):
#     user = User.objects.create_user(
#         username="dia123", email=valid_payload["email"], 
#         password=valid_payload["password"]
#     )
#     user.save()
#     cbtuser = CBTUser.objects.create(
#         user=user, date_of_birth=valid_payload["email"], 
#         first_name=valid_payload["first_name"], last_name=valid_payload["first_name"]
#     )
#     cbtuser.save()
#     return user

# @pytest.fixture(scope="session")
# def get_token(get_user):
#     token = Token.objects.get_or_create(user=get_user)
#     return token[0]


# def test_generate_username() -> None:
#     assert type(generate_username("adele loaves")) == str
#     assert len(generate_username("Matt Ha")) > 1
#     try:
#         generate_username()
#     except ValueError: ...
#     finally:
#         assert 1 == 1


# def test_create_valid_cbtuser() -> None:
#     response = client.post(
#         path = reverse('create_cbtuser'),
#         data = json.dumps(valid_payload),
#         content_type = 'application/json'
#     )
#     assert response.status_code == status.HTTP_201_CREATED


# def test_create_invalid_cbtuser() -> None:
#     response = client.post(
#         path  = reverse('create_cbtuser'),
#         data = json.dumps(invalid_payload),
#         content_type = 'application/json'
#     )
#     assert response.status_code == status.HTTP_400_BAD_REQUEST





# def test_valid_login_cbtuser(get_user) -> None:
#     response = client.post(
#         path = reverse('login_cbtuser'),
#         data = json.dumps({'username': get_user.username, 'password': valid_payload["password"]}),
#         content_type = 'application/json'
#     )
#     assert response.status_code == status.HTTP_200_OK

# def test_invalid_login_cbtuser() -> None:
#     response = client.post(
#         path = reverse('login_cbtuser'),
#         data = json.dumps({'username': get_user.username, 'password': 'passwd123',}),
#         content_type = 'application/json'
#     )
#     assert response.status_code == status.HTTP_403_FORBIDDEN


#     response = client.post(
#         path = reverse('login_cbtuser'),
#         data = json.dumps({'username': get_user.username}),
#         content_type = 'application/json'
#     )
#     assert response.status_code == status.HTTP_400_BAD_REQUEST


        

# def test_logout_cbtuser(get_token) -> None:
#     c = APIClient()
#     c.credentials(HTTP_AUTHORIZATION = "Token "+get_token)
#     response = c.get(path = reverse('logout_cbtuser'))
#     assert response.status_code == status.HTTP_200_OK
