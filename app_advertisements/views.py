from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse  # для отправки ответа на запрос пользователя
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth import get_user_model
from django.db.models import Count


def advertisement_detail(request, pk):  # работает с гет запросом, вытаскивает id и вставляем в ссылке вместо pk
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement, }
    return render(request, 'app_advertisements/advertisement.html', context)


def index(request):  # для принятия запроса
    title = request.GET.get('query')  # вытаскиваем заголовок для поиска
    if title:  # есть ли заголовок
        advertisements = Advertisement.objects.filter(title__icontains=title)  # выводим только объявления с нужным заголовком
    else:
        advertisements = Advertisement.objects.all()  # импортирует все объекты
    context = {'advertisements': advertisements,
                'title': title,
               }  # словарь для контекста
    return render(request, 'app_advertisements/index.html', context)  # добавляем контекст


User = get_user_model()


def top_sellers(request):  # открывает топ продавцов
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users': users, }
    return render(request, 'app_advertisements/top-sellers.html', context)


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

