from django.urls import path
from . import views

urlpatterns = [
    path("noteview/<str:i>", views.noteview, name="noteview"),
    path("noteadd/", views.noteadd, name="noteaddapi"),
    path("noteupdate/<str:i>", views.noteupdate, name="noteupdateapi"),
    path("del/<str:i>/", views.catdel, name="catdeleteapi"),
    path("notedelete/<str:i>/", views.notedel, name="notedeleteapi"),
]