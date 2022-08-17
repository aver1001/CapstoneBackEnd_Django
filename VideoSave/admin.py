from django.contrib import admin
from .models import VideoSave
# Register your models here.


@admin.register(VideoSave)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'user_video'
    ]
