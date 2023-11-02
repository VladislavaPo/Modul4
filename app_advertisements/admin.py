from django.contrib import admin  # работает с панелью админа\
from .models import Advertisement  # для получения данных из бд


class AdvertisementAdmin(admin.ModelAdmin):  # наследуем из род. класса работающего с админской панелью для переопределения структур
    # pass  # для тестирования
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'image']  # то что будет отображаться
    list_filter = ['auction', 'created_at']  # фильтрация по
    actions = ['make_auction_as_false', 'make_auction_as_true']  # какие-то быстрые действия
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes':  ['collapse']  # для отработки навыков сделаем возможным скрывать и раскрывать вкладку "Финансы"
        })
    )  # группировка полей на отдельные смысловые блоки

    @admin.action(description="Убрать возможность торга")  # декоратор
    def make_auction_as_false(self, request, queryset):  # чтобы указать каким объектом будем применять действия и что и как будем менять
        queryset.update(auction=False)  # чтобы указать каким объектом будем применять действия (название поля = чему будет равняться)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)  # регестрируем модель
