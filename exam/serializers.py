from rest_framework import serializers

from . models import Exam

class ExamSerializer(serializers.ModelSerializer):


    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'exam_code')
        # fields = '__all__'
