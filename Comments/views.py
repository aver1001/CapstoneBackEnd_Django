from django.shortcuts import render
from requests import request
from rest_framework.views import APIView
from .models import Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from .serializers import CommentSerializer
# Create your views here.


class CommentAPIView(APIView):
    queryset = Comment.objects.all()
    # permission_classes = []

    def post(self, requset):
        serializer = CommentSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)

        return Response(serializer.data)
