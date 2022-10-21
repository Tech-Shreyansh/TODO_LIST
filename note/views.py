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

def catdelete(request, i):
    cat = category.objects.get(id=i)
    if request.method == 'POST':
        cat.delete()
        return redirect('home')
    return render(request, "note/del_cat.html")

def notes(request):
    des= description.objects.all()
    context = {'desc' :des}
    return render(request, "note/notes.html", context)

def noteadd(request):
    form = noteform()
    if request.method == 'POST':
        form = noteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context = {'noteadd' : form}
    return render(request, "note/note_add.html", context)


def noteupdate(request, i):
    note = description.objects.get(id=i)
    form=noteform(instance=note)
    if request.method == 'POST':
        form = noteform(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context ={'noteupdate' : form}
    return render(request, "note/note_add.html", context)

def notedelete(request, i):
    note = description.objects.get(id=i)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, "note/delete.html")

def topicadd(request):
    form = topicform()
    if request.method == 'POST':
        form = topicform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noteadd')
    context = {'topicadd' : form}
    return render(request, "note/add_topic.html", context)