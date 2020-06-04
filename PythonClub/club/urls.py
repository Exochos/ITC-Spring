from django.urls import path, include
from .views import (
    getmeetings,
    getresources,
    index,
    meeting_details,
    newmeeting,
    loginmessage,
    logoutmessage
)

urlpatterns=[
    path('', index, name='index'),
    path('getmeetings/', getmeetings, name='meeting'),
    path('getresources/', getresources, name='resources'),
    path('meeting_details/<int:id>', meeting_details, name='meeting_details'),
    path('newmeeting/', newmeeting, name='newmeeting'),
    path('loginmessage/', loginmessage, name='loginmessage'),
    path('logoutmessage/', logoutmessage, name='logoutmessage'),
]