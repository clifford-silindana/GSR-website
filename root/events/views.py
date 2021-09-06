from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event
from .forms import EventForm

# Create your views here.

def index(request):
    totalEvents = Event.objects.all()
    total = len(list(totalEvents))
    context = {"totalEvents" : totalEvents, "total" : total}
    return render(request, "events/events.html", context)

def createEvent(request):
    form = EventForm()

    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("events:home"))
            

    context = {"form" : form}

    return render(request, "events/event_form.html", context)

def updateEvent(request, event_id):
    event = Event.objects.get(pk = event_id)
    form = EventForm(instance = event)

    if request.method == "POST":
        form = EventForm(request.POST, instance = event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("events:home"))

    context = {"form" : form, "event_id" : event_id}

    return render(request, "events/update.html", context)

def deleteEvent(request, event_id):

    event = Event.objects.get(pk = event_id)

    if request.method == "POST":
        event.delete()
        return HttpResponseRedirect(reverse("events:home"))


    context = {"event" : event}

    return render(request, "events/delete.html", context)






 
    
