from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model  # получение пользователей
from django.urls import reverse

User = get_user_model()  # хранит полученных пользователей


# класс для объявлений
class Advertisement(
    models.Model):  # для создания модели из класса нужно применить способ наследования - models.Model - превращаем класс в модель, а позже в таблипцу
    title = models.CharField("Заголовок",
                             max_length=128)  # (порядок: "альтернативное название", максимальное количество символос(принято обозначать в степени двойки))
    description = models.TextField("Описание")  # описание("альтернативное название")
    price = models.DecimalField("Цена", max_digits=10,
                                decimal_places=2)  # цена("альтернативное название", максимальное количество цифр всего и перед и за точкой, сколько знаков после точки)
    auction = models.BooleanField("Торг",
                                  help_text="Отметьте, если торг уместен")  # может ли быть скидка("альтернативное название", помощь/доп текст выведется при наведении)
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания(для автоматической записи времени один раз)
    updated_at = models.DateTimeField(
        auto_now=True)  # дата редактирования(автоматическая запись времени обновляющаяся при каждом изменении)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE,
                             null=True)  # хранит одного пользователя (переменная со всеми переменнами в связи один ко многим)
    image = models.ImageField("Изображение", upload_to="advertisements/")  # хранит путь до изображения

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})  # возвращает adv-detail и добавляет pk который заменяет на self.pk - мы передаем параметры

    @admin.display(description='Дата создания')
    def created_date(self):  # для того чтобы если время заявление создано сегодня то выводилось "Сегодня в ***"
        from django.utils import timezone  # библиотека работает только в этой функции
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')  # формат времени
            return format_html(
                '<span style="color: green; font-weight:bold;">Сегодня в {}</span>', created_time
            )  # отдельный стиль
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')  # если дата другая

    @admin.display(description='Дата изменения')  # дз
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime('%H:%M:%S')
            return format_html(
                '<span style="color: pink; font-weight:bold;">Сегодня в {}</span>', updated_date
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Изображение')  # дз м4.у5 картинка из ссылки в картинку
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )


    class Meta:
        db_table = "advertisements"  # поле для изменения названия таблицы

    def __str__(self):  # переопределение методов
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price}"  # когда мы используем эту функцию то нужно вывести
