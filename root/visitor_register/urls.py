from django.urls import path
from . import views

app_name = "visitor_register"

urlpatterns = [
    path("", views.index, name = "index"),
    path("newvisitor/", views.createVisitor, name = "newvisitor"),
    path("update/<int:student_id>/", views.updateVisitor, name = "updatevisitor"),
    path("delete/<int:student_id>/", views.deleteVisitor, name = "deleteVisitor")
]