from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mrngshow(request):
    return HttpResponse("Watch Old Movie")

def matinee(request):
    return HttpResponse("Watch Family Entertainer")

def secondshow(request):
    return HttpResponse("Watch Action Movie")