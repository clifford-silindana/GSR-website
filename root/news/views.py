from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import News
from .forms import NewsForm

# Create your views here.

def index(request):
    return render(request, "news/index.html")

def createNews(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thanks/")

    context = {"form" : form}
    return render(request, "news/news_form.html", context)


def thanks(request):
    return render(request, "news/thanks.html",)