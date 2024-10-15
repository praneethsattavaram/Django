from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.

def logic1(request):
    return HttpResponse("This is logic 1 from App 1")

def logic2(request):
    return HttpResponse("This is logic 2 from App 1")

def logic3(request):
    return HttpResponse("This is logic 3 from App 1")