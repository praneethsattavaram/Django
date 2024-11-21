from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_details, name="add_details"),
    path('list_details', views.list_details, name="list_details"),
    path('edit_details/<int:id>', views.edit_details, name="edit_details" ),
    path('delete_detail/<int:id>', views.delete_detail, name="delete_detail"),
    
]