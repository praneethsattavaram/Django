from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('8am', views.breakfast),
    path('1pm', views.lunch),
    path('7pm', views.dinner),
]
