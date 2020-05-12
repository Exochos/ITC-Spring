from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Meeting, Meeting_Minutes,Resources

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

# Return the details sub tab
#def meeting_details(request, id):
#    obj = get_object_or_404(Meeting, pk=id)
#    context = {
#        "title": "Detail",
#        "object": obj
#    }
#    return render(request, 'club/meeting_details.html', context)

def mdetails(request, id):
    m=get_object_or_404(Meeting, pk=id)
    context={
        'm' : m,
    }
    return render(request, 'mdetails.html', context=context)