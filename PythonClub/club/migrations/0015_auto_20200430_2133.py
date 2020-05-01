# Generated by Django 3.0.5 on 2020-05-01 04:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0014_remove_meeting_meeting_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='user_id',
        ),
        migrations.AddField(
            model_name='resources',
            name='user_id',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
