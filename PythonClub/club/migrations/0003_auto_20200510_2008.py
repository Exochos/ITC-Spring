# Generated by Django 2.2.12 on 2020-05-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20200505_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='id',
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]