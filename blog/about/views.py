from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menu(request):
    return HttpResponse("<h2>Welcome to the Menu</h2>")

def items(request):
    return HttpResponse("💝")