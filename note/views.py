from django.shortcuts import render
from .models import category,topic,description

# Create your views here.

def Home(request):
    categ= category.objects.all()
    context = {'cat' : categ}
    return render(request, "note/home.html", context)