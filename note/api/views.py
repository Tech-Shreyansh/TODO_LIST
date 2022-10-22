from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from note.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

def noteview(request, i):
    det = description.objects.get(id = i)
    ser = descriptionS(det)
    # data = JSONRenderer().render(ser.data)
    return JsonResponse(ser.data)