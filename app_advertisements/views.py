from django.shortcuts import render
from django.http import HttpResponse  # для отправки отввета на запрос пользователя


def index(request):  # для принятия запроса
    return HttpResponse('Все работает')  # сам ответ

