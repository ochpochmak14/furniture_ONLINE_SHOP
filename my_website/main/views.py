from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories
# Create your views here.

def index(request):
    
    categories = Categories.objects.all()
    
    dict = {
        'title': 'Home - Главная',
        'content': 'Главная страница магазина - HOME',
        'categories': categories
        
    }
    return render(request, "main/index.html", dict)

def about(request):
    dict = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': "Текст о том почему этот магазин классный."
        
    }
    return render(request, "main/about.html", dict)