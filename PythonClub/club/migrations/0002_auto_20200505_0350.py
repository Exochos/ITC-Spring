# Generated by Django 2.2.12 on 2020-05-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(max_length=250),
        ),
        migrations.AlterField(
            model_name='resources',
            name='URL',
            field=models.URLField(max_length=250),
        ),
        migrations.AlterField(
            model_name='resources',
            name='date_entered',
            field=models.DateField(),
        ),
    ]