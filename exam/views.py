import sys

from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Exam
from .serializers import ExamSerializer
from cbtuser.models import CBTUser


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_protect
def create_exam(request: HttpRequest) -> Response:
    """Create an Exam"""

    serializer = ExamSerializer(data=request.data)
    if serializer.is_valid():
        exam = Exam.objects.create(
            title = serializer.data.get("title"),
            description = serializer.data.get("description"),
            exam_manager = CBTUser.objects.get(user__username=request.user)
        )            
        exam.save()

        data = serializer.data.copy() #serializer is immutable so a copy to edit and display
        data["id"] = str(exam.id)
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def read_exam(request: HttpRequest, slug: str) -> Response:
    """Get exam info"""

    try:
        exam = Exam.objects.get(pk=slug)
    except Exam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExamSerializer(exam)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_protect
def update_exam(request: HttpRequest, slug: str) -> Response:
    """Get exam info and modify the values"""

    try:
        exam = Exam.objects.get(pk=slug)
    except Exam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExamSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Delete Exam
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_protect
def delete_exam(request: HttpRequest, slug: str) -> Response:
    """Delete exam and related info"""
    
    try:
        exam = Exam.objects.get(pk=slug)
        exam.delete()
        #TODO: Delete questions and results for this exam
        #       Make use of django signals to notify the other decoupled apps
        return Response(status=status.HTTP_200_OK)
    except Exam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

