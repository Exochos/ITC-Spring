from django.db import models
from django.contrib.auth.models import User


#Making a meeting model with the relevent fields 
class Meeting(models.Model):
	meeting_title = models.CharField(max_length=250)
	meeting_date  = models.CharField(max_length=250)
	meeting_time = models.CharField(max_length=250)
	meeting_location = models.CharField(max_length=250)
	meeting_agenda = models.CharField(max_length=250)


	def _str_(self):
		return self.name

	class Meta:
		db_table='meeting'
		verbose_name_plural='meeting'
