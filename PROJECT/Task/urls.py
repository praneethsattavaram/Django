from django.conf import settings
from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task', views.add_task, name='add_task'),
    path('view_task', views.view_task, name='view_task') 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)