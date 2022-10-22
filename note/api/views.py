from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from note.models import description,category, topic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def noteview(request, i):
    det = description.objects.get(id = i)
    ser = NotesSerializer(det)
    #data = JSONRenderer().render(ser.data)
    return Response(ser.data)

@api_view(['POST'])
def noteadd(request):
    ser = NotesSerializer(request.data)
    if ser.is_valid():
       ser.save()
    #data = JSONRenderer().render(ser.data)
    return Response(ser.data)

@api_view(['GET','PUT'])
def noteupdate(request, i):
    det = description.objects.get(id = i)
    ser = NotesSerializer(instance=det, data=request.data)
    #data = JSONRenderer().render(ser.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['GET'])
def Notes(request):
         Note = description.objects.all()

         searchResult = request.GET.get('s') or ''

         if searchResult:
            Note = Note.filter(topic__topic__icontains=s)

         ser = NotesSerializer(Note, many=True)
         return Response(se.data)

@api_view(['GET','DELETE'])
def catdel(request, i):
    categ = category.objects.get(id = i)
    categ.delete()
    return redirect('home')

@api_view(['GET','DELETE'])
def notedel(request, i):
    note = description.objects.get(id = i)
    note.delete()
    return redirect('notes')

