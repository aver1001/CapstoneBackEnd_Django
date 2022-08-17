from django.shortcuts import render
from rest_framework.response import Response
from .models import User, UserVideo
from rest_framework.views import APIView
from .serializers import UserSerializer, VideoSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
# Create your views here.


class UserListAPI(APIView):
    def get(self, requset):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserVideoAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # request.data['user_id'] = request.user
        request.data['user_id'] = request.user
        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
