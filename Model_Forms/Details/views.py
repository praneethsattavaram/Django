from django.shortcuts import render
from .forms import LaptopDetailsForm

# Create your views here.

def add_details(request):
    
    if request.method == "POST":
        form = LaptopDetailsForm(data = request.POST)
        if form.is_valid():
            form.save()

    form = LaptopDetailsForm()
    
    context = {
        'title' : 'Add Details',
        'form' : form,
    }
    return render(request, 'add_details.html', context)