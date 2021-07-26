from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CBTUser


class CBTUserSerializer(serializers.ModelSerializer):
    user: object 

    def __init__(self, instance=None, user=None, data=None, **kwargs):
        self.instance = instance
        if data is not None:
            data["user"] = user.id
            self.initial_data = data
        
        self.partial = kwargs.pop('partial', False)
        self._context = kwargs.pop('context', {})
        kwargs.pop('many', None)
        super(serializers.BaseSerializer, self).__init__(**kwargs)

    class Meta:
        model = CBTUser
        fields = "__all__"
        

class CBTLoginSerializer(serializers.Serializer):

    username = serializers.CharField(label="username", max_length=100)
    password = serializers.CharField(label="password", max_length=100)
