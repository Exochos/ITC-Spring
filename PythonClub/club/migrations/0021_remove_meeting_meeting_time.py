# Generated by Django 3.0.5 on 2020-05-01 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0020_auto_20200430_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='meeting_time',
        ),
    ]