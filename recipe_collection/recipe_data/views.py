from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Recipe

# Create your views here.


def add_recipe(request):
   
    if request.method == 'POST':
        r_title = request.POST['title']
        r_ingredients = request.POST['ingredients']
        r_time = request.POST['time']
        r_instructions = request.POST['instructions']
        Recipe.objects.create(Title=r_title, Ingredients = r_ingredients, Preparation_time = r_time, Instructions = r_instructions)  
        
    # recipe = Recipe.objects.all().order_by('id')
     
         
    context = {
        'title' : 'Recipes List',
        # 'recipes' : recipe,
        }

    return render(request, 'recipe_list.html', context)



def list_recipe(request, id):
    # try:
    #     Recipe.objects.get(id = id)
    # except:
    #     return HttpResponse("Data not found")
    
    recipe = Recipe.objects.all().order_by('id')
    
    context = {
        'recipes' : recipe,
        }
    
    return render(request, 'recipe_list.html', context)
