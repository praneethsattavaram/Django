from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about', views.menu),
    path('arg2', views.items),
]
