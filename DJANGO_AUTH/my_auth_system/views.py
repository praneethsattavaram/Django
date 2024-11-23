from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
            return render('login')
    
    else:
        return render(request, 'signup.html')
    
    

def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
            # return HttpResponse('Login Successful') 
        else:
            return render(request, 'login.html', {'msg': 'Invalid username or password'})

        
    return render(request, 'login.html')


def home_view(request):
    
    if request.user.is_authenticated:
        user = request.user
        context = {
            'username': user.username,
        }
        return render(request, 'home.html', context)
    else:
        return redirect('login')
        


def logout_view(request):
    logout(request)
    return redirect('login')

    