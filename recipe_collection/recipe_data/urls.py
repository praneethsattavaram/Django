from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_recipe, name='add_recipe'),
    # path('list_recipe/<int:id>', views.list_recipe, name='list_recipe'),
   
]
