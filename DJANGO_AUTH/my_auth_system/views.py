from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signup_view(request):
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        
        if password == conf_password:
            
            if User.objects.filter(username = username).exists():
                return render(request, 'signup.html', {'msg' : 'User already exists ! '})
            else:
                User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
            return HttpResponse('<h1> Account Created Successfully </h1>')
    
    else:
        return render(request, 'signup.html')