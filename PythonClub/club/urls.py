from django.urls import path, include
from .views import (
    getmeetings,
    getresources,
    index,
    meeting_details,
    newmeeting
)

urlpatterns=[
    path('', index, name='index'),
    path('getmeetings/', getmeetings, name='meeting'),
    path('getresources/', getresources, name='resources'),
    path('meeting_details/<int:id>', meeting_details, name='meeting_details'),
    path('newmeeting/', newmeeting, name='newmeeting'),
]