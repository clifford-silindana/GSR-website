from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("create/", views.createNews, name = "createNews"),
    path("update/<int:news_id>/", views.updateNews, name = "updateNews"),
    path("delete/<int:news_id>/", views.deleteNews, name = "deleteNews"),
]