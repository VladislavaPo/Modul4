from django.urls import path  # будет создавать саму ссылку и связывать
from .views import index  # импорт ответа пользователю/ представление

urlpatterns = [  # urlpatterns - обязательное/зарезервированное имя, массив ссылок
    path('', index)  # создали ссылку для метода views ссылка path с именем index
]
