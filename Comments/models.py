from django.db import models

# Create your models here.


class Comment(models.Model):
    content = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=5, null=False)
