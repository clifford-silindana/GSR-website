from django.shortcuts import render
from .forms import VisitorForm

# Create your views here.

def index(request):
    return render(request, "visitor_register/visitor.html")

def createVisitor(request):
    form = VisitorForm()
    context = {"form" : form}
    return render(request, "visitor_register/visitor_form.html", context)

def updateVisitor(request):
    context = {}
    return render(request, "visitor_register/update_form.html", context)