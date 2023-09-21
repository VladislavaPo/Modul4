from django.urls import path  # будет создавать саму ссылку и связывать
from .views import index, top_sellers  # импорт ответа пользователю/ представление

urlpatterns = [  # urlpatterns - обязательное/зарезервированное имя, массив ссылок
    path('', index, name='main-page'),   # создали ссылку для метода views ссылка path с именем index
    path('top-sellers/', top_sellers, name='top-sellers'),
]
