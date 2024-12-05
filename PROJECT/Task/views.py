from django.shortcuts import get_object_or_404, redirect, render
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
        return redirect('view_task')
    else:
        form = TaskForm(initial={'user':request.user})
    context = {
        'title' : 'Add Task',
        'form' : form
    }
    return render(request, 'add_task.html', context)



@login_required
def view_task(request):    
    tasks = Task.objects.filter(user=request.user)
    completed_tasks = tasks.filter(completed=True)
    pending_tasks = tasks.filter(completed=False)

    context = {
        'title': 'View Task',
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    }
    return render(request, 'view_task.html', context)


@login_required
def update_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except:
        pass 
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  
        if form.is_valid():
            form.save()  
            return redirect('view_task')  
    else:
        form = TaskForm(instance=task)  
    
    context = {
        'title': 'Update Task',
        'form': form
    }
    return render(request, 'update_task.html', context)


@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = True 
    task.save()
    return redirect('view_task')

@login_required
def delete_task(request, id):
    try:
        data = Task.objects.get(id=id)
    except:
        pass
    data.delete()
    return redirect('view_task')