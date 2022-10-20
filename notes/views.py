from django.shortcuts import render
from .models import trial
# from django.http import HttpResponse

# Create your views here.

def Home(request):
    section = trial.objects.all()
    context= {'sectionss' : section}
    return render(request, "notes/index.html", context )

def rooms(request):
    return render(request, "notes/rooms.html")

def room(request,ik):
    section = trial.objects.get(id=ik)
    cont= {'sections' : section}
    return render(request, "notes/room.html", cont )