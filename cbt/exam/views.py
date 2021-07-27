from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.response import Response

from .models import Exam

# Create your views here.

# create Exam
def create(request: HttpRequest) -> Response:
    """Create a new Exam
    :param request: HttpRequest
    :return: Response
    """

    pass

# Read Exam
# Edit Exam
# Delete Exam