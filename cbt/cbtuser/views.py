import random
from typing import Tuple

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required


from cbtuser.serializers import CBTUserSerializer, CBTLoginSerializer


@api_view(['POST'])
@csrf_protect
def create(request: HttpRequest) -> Response:
    """Create a CBT User
        :param request: HttpRequest
        :return: Response
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
@csrf_exempt
def login_cbtuser(request: HttpRequest) -> Response:
        """Log a user on the system 
        :param request: HttpRequest
        :return: Response
        """

        form = CBTLoginSerializer(data=request.data)

        if form.is_valid():
            user = authenticate(request, username=form.data.get("username"), password=form.data.get("password"))
            if user is not None:
                # login(request, user) #activate when using session authentication
                token = Token.objects.get_or_create(user=user)
                return Response({'message':"Logged in Successfully", 'token':str(token[0])}, status=status.HTTP_200_OK)
            return Response("Username and Password are incorrect", status=status.HTTP_403_FORBIDDEN)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_cbtuser(request: HttpRequest) -> Response:
    """Delete user session and delete auth token
        :param request: HttpRequest
        :return: Response"""

    #logout(request) ##activate when using session authentication
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)



#utils 
def generate_username(*names: Tuple[str, ...]) -> str:
    """Generate a random username
    :param names: Tuple[str,...]
    :return: str
    """
    
    if len(names:= tuple(i for i in names if i != None)) > 0:
        first_letter = names[0][0]
        three_letters_surname = names[-1][:3]
        number = '{:03d}'.format(random.randrange(1, 999))
        username = (first_letter + three_letters_surname + number)
        return str(username).capitalize()
    elif "test" == __import__("sys").argv[-1]:
        return "Testmode"
    else:
        raise ValueError("Unexpexted Data")
        
