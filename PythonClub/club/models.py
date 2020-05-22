from django.db import models
from django.contrib.auth.models import User


#Making a meeting model with the relevent fields.
class Meeting(models.Model):
	meeting_title = models.CharField(max_length=250)
	meeting_date = models.DateField()
	meeting_time = models.TimeField()
	meeting_location = models.CharField(max_length=250)
	meeting_agenda = models.CharField(max_length=250)
	meeting_id = models.IntegerField(primary_key=True)
	def __str__(self):
		return self.meeting_title
	class Meta:
		db_table='meeting'
		verbose_name_plural='meeting'


#Minutes model here with various values
class  Meeting_Minutes(models.Model):
	meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
	attendance = models.ManyToManyField(User)
	minutes_text = models.CharField(max_length=2000)
	def __str__(self):
		return self.minutes_text


# Meeting Resources
class Resources(models.Model):
        resource_name = models.CharField(max_length=250)
        resource_type = models.CharField(max_length=250)
        URL = models.URLField(max_length=250)
        date_entered = models.DateField()
        user_id = models.ManyToManyField(User)
        description = models.CharField(max_length = 500)
        def __str__(self):
                return self.resource_name
        class Meta:
                db_table = 'resources'
                verbose_name_plural = 'resources'

class Event(models.Model):
        event_title = models.CharField(max_length=250)
        location = models.CharField(max_length=250)
        date_time = models.DateTimeField(max_length=250)
        user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
        description = models.CharField(max_length=250)
        def __str__(self):
                return self.event_title
        class Meta:
                db_table = 'event'
                verbose_name_plural = 'event'