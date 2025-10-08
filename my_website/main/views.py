from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    dict = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True
    }
    return render(request, "main/index.html", dict)

def about(request):
    return HttpResponse('About Page')