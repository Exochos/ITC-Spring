from django.db import models
from django.contrib.auth.models import User


# Making a meeting model with the relevent fields and such
#
class Meeting(models.Model):
#	meeting_title = models.CharField(max_length=250)
#	meeting_date  = models.CharField(max_length=250)
#	meeting_time = models.CharField(max_length=250)
#	meeting_location = models.CharField(max_length=250)
	meeting_agenda = models.CharField(max_length=250)
	def _str_(self):
		return self.name
	class Meta:
		db_table='meeting'
		verbose_name_plural='meeting'

# Meeting Minutes 
class Meeting_Minutes(models.Model):
	# What is this magic? --v
	meeting_id = models.ForeignKey(Meeting, on_delete = models.CASCADE)
	attendance = models.ManyToManyField(User)
	minutes_text = models.CharField(max_length = 20000)
	def _str_(self):
		return self.name
	class Meta:
		db_table='meeting_minutes'
		verbose_name_plural='meeting minutes'

# Meeting Resources
class Resources(models.Model):
	resource_name = models.CharField(max_length=250)
	resource_type = models.CharField(max_length=250)
	URL = models.CharField(max_length=250)
	date_entered = models.CharField(max_length=250)
	user_id = models.ManyToManyField(User)
	description = models.CharField(max_length = 500)
	def _str_(self):
		return self.name
	class Meta:
		db_table = 'resources'
		verbose_name_plural = 'resources'

class Event(models.Model):
	event_title = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	date_time = models.CharField(max_length=250)
	user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	description = models.CharField(max_length=250)
	def _str_(self):
		return self.name
	class Meta:
		db_table = 'event'
		verbose_name_plural = 'event'