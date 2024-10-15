from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Logic1', views.logic1),
    path('Logic2', views.logic2)
]
