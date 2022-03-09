from django.shortcuts import render
from recipes.models import Recipe
from django.http import Http404
from utils.recipe.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

    
def category(request, category_id):
    
    recipes = Recipe.objects.filter(category__id = category_id, is_published=True).order_by('-id')
    if not recipes:
        raise Http404('Not Found')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': recipes.first().category.name,
    })    
    

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page':True,
    })