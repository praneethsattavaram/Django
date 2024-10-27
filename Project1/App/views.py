from django.shortcuts import render

# Create your views here.

tasks = [
    {
        'id' : 1,
        'name' : 'Chatting',
        'desc' : 'Chatting is very sensitive topic Chat only when it is needed or important'
    },
    {
        'id' : 2,
        'name' : 'Instagram',
        'desc' : 'Instagram is a social media app to which youth got addicted a lot'
    },
    {
        'id' : 3,
        'name' : 'SnapChat',
        'desc' : 'SnapChat is used to capture our current moments and share them with your friends'
    }
]

def base(request):
    return render(request, 'base.html')


def home(request):
    
    context = {
        'title' : 'Home Page',
        'tasks' : tasks,
    }
    return render(request, 'pages/home.html', context)


def task(request, id):
    
    for task in tasks:
        if task['id'] == id:
            task_ = task
            
    context = {
        'task1' : task_
    }
    
    return render(request, 'pages/task.html', context)


def about(request):
    context = {
        'title' : 'About Page',
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {
        'title' : 'Contact Page',
    }
    return render(request, 'pages/contact.html', context)