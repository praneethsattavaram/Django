from django.urls import path
from . import views

urlpatterns = [
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('list_recipe/', views.list_recipe, name='list_recipe'),
    path('update_recipe<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete_recipe<int:id>/', views.delete_recipe, name='delete_recipe'),
]
