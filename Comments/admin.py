from django.contrib import admin
from .models import Comment

# Register your models here.


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'content',
    ]
