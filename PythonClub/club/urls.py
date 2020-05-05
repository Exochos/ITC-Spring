from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='meeting'),
    path('getresources/', views.getresources, name='resources'),
]



