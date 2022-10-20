from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("add/",views.add_cat, name="add"),
    path("notes/", views.notes, name="notes"),
    path("noteadd/", views.noteadd, name="noteadd"),
    path("topicadd/", views.topicadd, name="topicadd"),
]