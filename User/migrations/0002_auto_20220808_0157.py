# Generated by Django 3.2.10 on 2022-08-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
