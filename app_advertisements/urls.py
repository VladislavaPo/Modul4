from django.urls import path  # будет создавать саму ссылку и связывать
from .views import index, top_sellers, advertisement_post, advertisement_detail  # импорт ответа пользователю/ представление

urlpatterns = [  # urlpatterns - обязательное/зарезервированное имя, массив ссылок
    path('', index, name='main-page'),   # создали ссылку для метода views ссылка path с именем index
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/',    advertisement_post,    name='adv-post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail')  # новый особый изменяемый адрес, <int:pk> - какой-то обязательный параметр в нашем случае цифра
]
