# Generated by Django 3.0.5 on 2020-05-01 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_auto_20200501_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]