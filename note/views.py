from django.shortcuts import render, redirect
from .models import category,topic,description
from .forms import catform, noteform, topicform

# Create your views here.

def Home(request):
    categ= category.objects.all()
    context = {'cat' : categ}
    return render(request, "note/home.html", context)

def add_cat(request):
    form = catform()
    if request.method == 'POST':
        form = catform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'addcat' : form}
    return render(request, "note/add_cat.html", context)

def notes(request):
    categ= category.objects.all()
    top= topic.objects.all()
    des= description.objects.all()
    context = {'desc' :des}
    return render(request, "note/notes.html", context)

def noteadd(request):
    form = noteform()
    if request.method == 'POST':
        form = noteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'noteadd' : form}
    return render(request, "note/note_add.html", context)

def topicadd(request):
    form = topicform()
    if request.method == 'POST':
        form = topicform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noteadd')
    context = {'topicadd' : form}
    return render(request, "note/add_topic.html", context)
    
