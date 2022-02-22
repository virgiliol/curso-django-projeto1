from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # return response
    return render(request, 'global/home.html')


def sobre(request):
    # return response
    return HttpResponse('sobre')


def contato(request):
    # return response
    return HttpResponse('contato')
