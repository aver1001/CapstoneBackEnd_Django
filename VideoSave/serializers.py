from rest_framework import serializers
from .models import VideoSave


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSave
        fields = '__all__'
