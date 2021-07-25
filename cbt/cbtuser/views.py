import random
from typing import OrderedDict

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from django.contrib.auth.models import User

from cbtuser.serializers import CBTUserSerializer
from cbtuser.models import CBTUser


@api_view(['POST'])
def create(request: HttpRequest) -> Response:
    """Create a CBT User
        request:    HttpRequest
        return:     Response
    """


    # create a User object
    user = User.objects.create_user(
        username = generate_username(request.data.get("first_name"), 
                                    request.data.get("last_name")),
        email = request.data.get("email"),
        password = request.data.get("password")
    )
    user.save()

    serializer = CBTUserSerializer(user=user, data=request.data.copy()) #refer to the __init__ in serializers.py
    if serializer.is_valid():
        serializer.save()
        return Response("User Created", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request: HttpRequest) -> Response:

        pass

#utils 
def generate_username(*names):
    """Generate a random username
    """
    first_letter = names[0][0]
    three_letters_surname = names[-1][:3]
    number = '{:03d}'.format(random.randrange(1, 999))
    username = (first_letter + three_letters_surname + number)
    return str(username).capitalize()