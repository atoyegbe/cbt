from django.db.models.fields import UUIDField
from rest_framework import serializers

from question.models import Question

class QuestionSerializer(serializers.ModelSerializer):

    correct_option = serializers.UUIDField(required=False)

    class Meta:
        model = Question
        fields = "__all__"
