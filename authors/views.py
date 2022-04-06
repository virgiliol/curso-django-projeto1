from django.shortcuts import render

# Create your views here.

def register_view(request):
    render(request, 'authors/pages/register_view.html')

