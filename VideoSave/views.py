from django.shortcuts import render
from rest_framework.response import Response
from .models import VideoSave
from rest_framework.views import APIView
from .serializers import VideoSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .tasks import Check

# Create your views here.


class SaveVideoAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = VideoSave.objects.filter(user_id=request.user.id)
        serializer = VideoSerializer(data, many=True)
        Check.delay()
        return Response(serializer.data)

    def post(self, request):
        request.data['user_id'] = request.user.id
        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
