from django.db import models


# класс для объявлений
class Advertisement(models.Model):  # для создания модели из класса нужно применить способ наследования - models.Model - превращаем класс в модель, а позже в таблипцу
    title = models.CharField("Заголовок", max_length= 128)  # (порядок: "альтернативное название", максимальное количество символос(принято обозначать в степени двойки))
    description = models.TextField("Название")  # описание("альтернативное название")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)  # цена("альтернативное название", максимальное количество цифр всего и перед и за точкой, сколько знаков после точки)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")  # может ли быть скидка("альтернативное название", помощь/доп текст выведется при наведении)
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания(для автоматической записи времени один раз)
    updated_at = models.DateTimeField(auto_now=True)  # дата редактирования(автоматическая запись времени обновляющаяся при каждом изменении)

    class Meta:
        db_table = "advertisements"  # поле для изменения названия таблицы
