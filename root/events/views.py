from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm

# Create your views here.

def index(request):
    totalEvents = Event.objects.all()
    context = {"totalEvents" : totalEvents}
    return render(request, "events/events.html", context)

def createEvent(request):
    form = EventForm()

    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            

    context = {"form" : form}

    return render(request, "events/event_form.html", context)

 
    
