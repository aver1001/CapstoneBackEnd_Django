# Generated by Django 3.2.10 on 2022-08-08 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20220808_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(db_column='user_name', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='User.user')),
            ],
        ),
    ]
