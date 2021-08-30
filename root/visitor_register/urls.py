from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("newvisitor/", views.createVisitor, name = "newvisitor"),
    path("updatevisitor/", views.updateVisitor, name = "updatevisitor")
]