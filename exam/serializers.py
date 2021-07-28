import sys

from rest_framework import serializers

from . models import Exam

class ExamSerializer(serializers.ModelSerializer):


    class Meta:
        model = Exam
        fields = ('id', 'title', 'description')
        # fields = '__all__'
