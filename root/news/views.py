from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import News
from .forms import NewsForm

# Create your views here.

def index(request):
    totalNews = News.objects.all()
    totalNewsNumber = len(list(totalNews))
    context = {"totalNewsNumber" : totalNewsNumber, "totalNews" : totalNews}
     
    return render(request, "news/index.html", context)

def createNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

    form = NewsForm()

    context = {"form" : form}
    return render(request, "news/news_form.html", context)

def updateNews(request, news_id):
    news = News.objects.get(pk = news_id)

    form = NewsForm(instance = news)

    if request.method == "POST":
        form = NewsForm(request.POST, instance = news)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))

    

    context = {"news_id" : news_id, "form" : form}
    return render(request, "news/update.html", context)

def deleteNews(request, news_id):

    if request.method == "POST":
        news = News.objects.get(pk = news_id)
        news.delete()
        return HttpResponseRedirect(reverse("index"))
        
    context = {"news_id" : news_id}
    return render(request, "news/delete.html", context)

