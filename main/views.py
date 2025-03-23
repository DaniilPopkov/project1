
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):
   
    context ={
        'title': 'Ресторан Sunrise - Главная',
        'content':"Ресторан Sunrise",
        
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context ={
        'title': 'Ресторан Sunrise - О нас',
        'content':"О нас",
        'text_on_page':"«Загляните в Sunrise, где тепло солнца отражается в нашей уютной атмосфере и тщательно продуманном меню. Мы предлагаем широкий выбор блюд, от классической классики до смелых, инновационных творений, приготовленных из лучших ингредиентов с капелькой страсти. Каждое посещение Sunrise — это возможность насладиться моментом и пробудить свой вкус». ",
        
    }
    return render(request, 'main/about.html', context)

