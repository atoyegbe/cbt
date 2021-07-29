import uuid
from copy import copy

from django.db.models.fields import UUIDField
from django.db.utils import Error

from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from question.models import Question
from exam.models import Exam
from question.serializers import QuestionSerializer


# create
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_protect
def create_question(request: HttpRequest, exam) -> Response: 
    """Create an Question"""

    request.data['exam'] = exam # str(Exam.objects.get(pk=exam).id)
    # if the correct option id was given with the question
    try:
        temp = str(request.data.get('correct_option')) or ""
        if len(temp) == 36: #length of uuid4 is 36   
            temp = uuid.UUID(temp)
            request.data['correct_option'] = temp
        else:
            request.data.pop('correct_option')

    except ValueError:
        # if it wasn't the serializer knows it not required
        return Response({"message":"inspect the variable in request"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = QuestionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# edit
# upload from file
# view
