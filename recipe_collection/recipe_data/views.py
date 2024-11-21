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
        return redirect('list_recipe')
    context = {
        'title' : 'Add Recipe',     
        }

    return render(request, 'recipe_create.html', context)



def list_recipe(request):
    
    recipes = Recipe.objects.all().order_by('id')
    
    search = request.GET.get('search')
    if search:
        recipes = Recipe.objects.filter(Title__icontains=search)
    
    for recipe in recipes:
        print(recipe.Preparation_time)
        
    context = {
        'title' : 'Recipes list',
        'recipes' : recipes,
        'search'  : search,
        }
    
    return render(request, 'recipe_list.html', context)


def update_recipe(request, id):
    try:
        recipe = Recipe.objects.get(id = id)
    except:
        return HttpResponse("Recipe not found")
    
    if request.method == "POST":
        recipe.Title = request.POST['title']
        recipe.Ingredients = request.POST['ingredients']
        recipe.Preparation_time = request.POST['time']
        recipe.Instructions = request.POST['instructions']
        recipe.save()
        
        return redirect('list_recipe')
    
    context = {
        'title' : 'Update Recipe',
    } # type: ignore
    
    return render(request, 'recipe_update.html', context)


def delete_recipe(request, id):
    try:
        recipe = Recipe.objects.get(id = id)
    except:
        return HttpResponse("Recipe not found")
    
    recipe.delete()
    return redirect('list_recipe')
