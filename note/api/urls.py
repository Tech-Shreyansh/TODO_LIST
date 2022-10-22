from django.urls import path
from . import views

urlpatterns = [
    path("noteview/<str:i>", views.noteview, name="noteview"),
]