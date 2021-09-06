from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name = "login"),
    path("home/<int:student_id>/", views.index, name = "home")
]