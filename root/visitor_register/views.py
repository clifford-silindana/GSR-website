from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Visitor
from .forms import VisitorForm

# Create your views here.

def index(request):
    visitors = Visitor.objects.all()
    numberOfVisitors = len(list(visitors))
    context = {"visitors" : visitors, "numberOfVisitors" : numberOfVisitors}
    return render(request, "visitor_register/index.html", context)

def createVisitor(request):
    form = VisitorForm()

    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("visitor_register:index"))

    context = {"form" : form}
    return render(request, "visitor_register/visitor_form.html", context)

def updateVisitor(request, student_id):
    visitor = Visitor.objects.get(pk = student_id)

    form = VisitorForm(instance = visitor)

    if request.method == "POST":
        form = VisitorForm(request.POST, instance = visitor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("visitor_register:index"))

    context = {"student_id" : student_id, "form" : form}
    return render(request, "visitor_register/update.html", context)

def deleteVisitor(request, student_id):
    visitor = Visitor.objects.get(pk = student_id)

    if request.method == "POST":
        visitor.delete()
        return HttpResponseRedirect(reverse("visitor_register:index"))


    context = {"student_id" : student_id}
    return render(request, "visitor_register/delete.html", context)