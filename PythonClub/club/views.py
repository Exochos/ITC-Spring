from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    ListView,
)
from .models import (
    Meeting,
    Meeting_Minutes,
    Resources,
    Event,
)
from .forms import MeetingForm


# This is our new meeting form function
def newmeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm
        else:
            form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

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

def meeting_details(request,id):
    obj = get_object_or_404(Meeting, pk=id)
    context = {
        "object": obj
    }
    return render(request, "club/meeting_details.html", context)

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')

@login_required
def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'club/newmeeting.html', {'form': form})