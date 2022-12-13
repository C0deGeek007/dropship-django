from rest_framework import serializers
# from .models import UserModel
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model= get_user_model()
        fields='__all__'

    def create(validated_data):
        return get_user_model().objects.create_user(validated_data['refId'], validated_data['password'],ex=validated_data['ex'])


class loginSerializer(serializers.Serializer):
    refId = serializers.EmailField()
    password = serializers.CharField(max_length=200)

class loginResponseSerializer(serializers.Serializer):
    refId = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    id = serializers.IntegerField()

