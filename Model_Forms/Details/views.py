from django.shortcuts import redirect, render
from .forms import LaptopDetailsForm
from .models import LaptopDetails

# Create your views here.

def add_details(request):
    
    if request.method == "POST":
        form = LaptopDetailsForm(data = request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('list_details')
    
    form = LaptopDetailsForm()
    
    context = {
        'title' : 'Add Details',
        'form' : form,
    }
    
    return render(request, 'add_details.html', context)




def list_details(request):
    
    data = LaptopDetails.objects.all()
    
    context = {
        'title' : 'Laptop Details',
        'data' : data
    }
    
    return render(request, 'list_details.html', context)


def edit_details(request, id):
    
    try:
        data = LaptopDetails.objects.get(id=id)
    except:
        pass
    
    if request.method == "POST":
        form = LaptopDetailsForm(data = request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect('list_details')
    
    form = LaptopDetailsForm(instance=data)
    
    context = {
        'title' : 'Edit Details',
        'form' : form,
    }
    
    return render(request, 'edit_details.html', context)

        
def delete_detail(request, id):
    
    try:
        data = LaptopDetails.objects.get(id=id)
    except:
        pass
    
    data.delete()
    
    return redirect('list_details')