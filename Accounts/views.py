from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer


class SignupAPIView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
