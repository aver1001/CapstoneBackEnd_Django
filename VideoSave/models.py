from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class VideoSave(models.Model):
    user_id = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE, db_column='user_name')
    user_video = models.FileField(upload_to='Video', null=False, default='/')
