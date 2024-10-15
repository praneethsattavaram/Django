from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def breakfast(request):
    return HttpResponse("Eat Idly or Dosa with Sambar")

def lunch(request):
    return HttpResponse("Eat Sambar Rice with Papad and Coconut Chutney")

def dinner(request):
    return HttpResponse("Eat Sambar Rice with omlette")