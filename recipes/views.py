from django.shortcuts import render

# Create your views here.


def home(request):
    # return response
    return render(request, 'recipes/pages/home.html')
