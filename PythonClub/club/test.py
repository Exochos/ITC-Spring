from django.test import TestCase
from club.models import Meeting, Meeting_Minutes, Resources, Event 
from club.forms import MeetingForm

class MeetingTest(TestCase):
    def test_string(self):
        meeting=Meeting(meeting_title="Meetingz")
        self.assertEqual(str(meeting), meeting.meeting_title)
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinutesTest(TestCase):
    def test_string(self):
        minutes=Meeting_Minutes(minutes_text='Test Test Test')
        self.assertEqual(str(minutes), minutes.minutes_text)

class ResourcesTest(TestCase):
	def test_string(self):
		resources=Resources(resource_name="Resources Test")
		self.assertEqual(str(resources), resources.resource_name)
	
	def test_tablename(self):
		self.assertEqual(str(Resources._meta.db_table), 'resources')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(event_title='Event Test')
        self.assertEqual(str(event), event.event_title)

class NewMeetingFormTest(TestCase):

    def test_MeetingForm(self):
        form = MeetingForm(data={'meeting_title':"TestTestTest1", 'meeting_date':"2020-06-04", 'meeting_time':"09:00:00", 'meeting_location':"Home", 'meeting_agenda':"Testing forms", 'meeting_id':"10"})
        self.assertTrue(form.is_valid())
