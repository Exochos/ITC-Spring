from django import forms
from .models import Meeting, Meeting_Minutes, Resources, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'
        