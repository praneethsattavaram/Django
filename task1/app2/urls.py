from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('8am', views.mrngshow),
    path('11am', views.matinee),
    path('10pm', views.secondshow),
]
