from django.shortcuts import render
from .models import Meeting, Meeting_Minutes,Resources

def gettypes(request):
    meeting_list = Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list' : meeting_list})
def getresources(request):
    resources = Resources.objects.all()
    return render(request, 'club/resources.html', {'resources' : resources})
# Create your views here.
def index (request):
    return render(request, 'club/index.html')
