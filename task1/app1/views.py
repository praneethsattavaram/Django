from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def logic1(request):
    return HttpResponse("This is logic 1 from App1")

def logic2(request):
    return HttpResponse("This is logic 2 from App 1")