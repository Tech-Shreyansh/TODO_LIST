from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("rooms/",views.rooms, name ="rooms"),
    path("room/<str:ik>/",views.room, name ="room"),
]