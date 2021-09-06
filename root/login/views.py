from django.shortcuts import render
from .models import Login
from .forms import LoginForm

# Create your views here.

def login(request):
    form = LoginForm()
    context = {"form" : form}

    return render(request, "login/login.html", context)

def index(request, student_id):
    student = Login.objects.get(pk = student_id)
    student_name = student.username
    context = {"student_name" : student_name}
    return render(request, "login/index.html", context)
