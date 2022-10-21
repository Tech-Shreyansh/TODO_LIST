from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("add/",views.add_cat, name="add"),
    path("del/<str:i>/", views.catdelete, name="catdelete"),
    path("notes/", views.notes, name="notes"),
    path("noteadd/", views.noteadd, name="noteadd"),
    path("noteupdate/<str:i>/", views.noteupdate, name="noteupdate"),
    path("notedelete/<str:i>/", views.notedelete, name="notedelete"),
    path("topicadd/", views.topicadd, name="topicadd"),
]