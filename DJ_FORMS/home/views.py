from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Studentform
from .models import Student

# Create your views here.

def home(request):
    
    if request.method == 'POST':
        form = Studentform(data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            usn = form.cleaned_data['usn']
            mobile = form.cleaned_data['mobile']
            course = form.cleaned_data['course']
            
            Student.objects.create(name=name, usn=usn, mobile = mobile, course = course) 
    
    Data  = Student.objects.all()
    forms = Studentform()
     
    context = {
        'title' : 'Forms',
        'form' : forms,
        'data' : Data,
    }
    
    return render(request, 'home.html', context)


def update(request,id):
    
    try:
        update = Student.objects.get(id=id)
    except:
        return HttpResponse("Data not found")
    
    
    if request.method == 'POST':
        form = Studentform(data = request.POST)
        if form.is_valid():
            update.name = form.cleaned_data['name']
            update.usn = form.cleaned_data['usn']
            update.mobile = form.cleaned_data['mobile']
            update.course = form.cleaned_data['course']
            update.save() 
    
        return redirect("home")
    
    forms = Studentform()
    
    context = {
        'title' : 'Update Form',
        'form' : forms,
       
    }
    
    return render(request, "update.html", context)



def delete(request,id):
    
    try:
        data = Student.objects.get(id=id)
    except:
        return HttpResponse("Data not found")
    
    data.delete()
    
    return redirect('home')