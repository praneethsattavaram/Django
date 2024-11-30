from django.shortcuts import render
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    
    context = {
        'title' : 'Home'
    }
    return render(request, 'home.html', context)

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(initial={request.user})
    context = {
        'title' : 'Add Task',
        'form' : form
    }
    return render(request, 'add_task.html', context)
        