from django.shortcuts import render
from .forms import TaskForm, Task
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
        form = TaskForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(initial={'user':request.user})
    context = {
        'title' : 'Add Task',
        'form' : form
    }
    return render(request, 'add_task.html', context)


@login_required
def view_task(request):    
    task = Task.objects.filter(user = request.user)
    context = {
        'title': 'View Task',
        'tasks' : task  
    }
    return render(request, 'view_task.html', context)


        