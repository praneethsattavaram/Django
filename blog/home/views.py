from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Created home page")

def index(request):
    return HttpResponse("<h1> We are inside index page</h1>")