from django.shortcuts import render
from django.http import HttpResponse  # для отправки отввета на запрос пользователя


def index(request):  # для принятия запроса
    # return HttpResponse('Все работает')  # сам ответ в виде текста
    return render(request, 'index.html')  # ответ в виде html файла index


def top_sellers(request):  # открывает топ продовцов
    return render(request, 'top-sellers.html')
