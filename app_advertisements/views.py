from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse  # для отправки ответа на запрос пользователя
from .models import Advertisement
from .forms import AdvertisementForm


def index(request):  # для принятия запроса
    advertisements = Advertisement.objects.all()  # импортирует все объекты
    context = {'advertisements': advertisements}  # словарь для контекста
    # return HttpResponse('Все работает')  # сам ответ в виде текста
    # return render(request, 'index.html')  # ответ в виде html файла index
    return render(request, 'app_advertisements/index.html', context)  # добавляем контекст


def top_sellers(request):  # открывает топ продавцов
    return render(request, 'app_advertisements/top-sellers.html')


def advertisement_post(request):  # работает со страницей "разместить объявление"
    if request.method == "POST":  # если перед нами POST запрос(мы получаем данные)
        form = AdvertisementForm(request.POST, request.FILES)  # чтобы хранить то что получили - вытягиваем все данные из запроса
        if form.is_valid():  # проверяем на валидность - работоспособность данных, правильно ли форма заполнена
            advertisement = form.save(commit=False)  # сохраняет всю форму(последнее сохранение не записывается)
            advertisement.user = request.user  # ставит вместо "пользователя" пользователя который последний над ней работал
            advertisement.save()
            url = reverse('main-page')  # создает ссылку на домашнюю ссылку
            return redirect(url)  # открывает домашнюю страницу и отправляет туда
    else:  # если запрос неправильный
        form = AdvertisementForm()
    context = {'form': form}  # должно работать всегда
    return render(request, 'app_advertisements/advertisement-post.html', context)

