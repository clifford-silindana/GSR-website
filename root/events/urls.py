from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("", views.index, name = "home"),
    path("createevent/", views.createEvent, name = "createEvent"),
    path("update/<int:event_id>/", views.updateEvent, name = "updateDelete"),
    path("delete/<int:event_id>/", views.deleteEvent, name = "deleteEvent"),

]