from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, primary_key=True)
    user_password = models.CharField(max_length=30)
    user_email = models.EmailField(unique=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'User'
        verbose_name = '유저'
        verbose_name_plural = '유저'


class UserVideo(models.Model):
    user_id = models.ForeignKey(
        "User", related_name="user", on_delete=models.CASCADE, db_column='user_name')
    user_video = models.FileField(upload_to='Video', null=False, default='/')
