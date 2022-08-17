from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, data):
        user = User.objects.create(
            username=data['username'], email=data['email'])
        user.set_password(data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
