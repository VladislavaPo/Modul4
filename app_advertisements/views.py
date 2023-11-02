from django.shortcuts import render
from django.http import HttpResponse  # для отправки отввета на запрос пользователя
from .models import Advertisement


def index(request):  # для принятия запроса
    advertisements = Advertisement.objects.all()  # импортирует все объекты
    context = {'advertisements': advertisements}  # словарь для контекста
    # return HttpResponse('Все работает')  # сам ответ в виде текста
    # return render(request, 'index.html')  # ответ в виде html файла index
    return render(request, 'index.html', context)  # добавляем контекст


def top_sellers(request):  # открывает топ продовцов
    return render(request, 'top-sellers.html')
