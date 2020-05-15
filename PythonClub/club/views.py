from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import (
    Meeting,
    Meeting_Minutes,
    Resources,
    Event,
)
# Return the meetings tab
def getmeetings(request):
    meeting = Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting' : meeting})

# Return the resources tab
def getresources(request):
    resources = Resources.objects.all()
    return render(request, 'club/resources.html', {'resources' : resources})

# Return the index.
def index (request):
    return render(request, 'club/index.html')

def meeting_details(request, id):
    obj = get_object_or_404(Meeting, pk=id)
    context = {
        "object": obj
    }
    return render(request, "club/meeting_details.html", context)