from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("createnews/", views.createNews, name = "createnews")
]