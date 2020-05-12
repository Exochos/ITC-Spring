from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getmeetings/', views.getmeetings, name='meeting'),
    path('getresources/', views.getresources, name='resources'),
    path('mdetails/<int:id>', views.mdetails, name='mdetails')
    #path('meeting_details/<int:id>', views.meeting_details, name='meeting_details'),
]



