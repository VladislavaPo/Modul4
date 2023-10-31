from django.apps import AppConfig


class AppAdvertisementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_advertisements'
    verbose_name = 'Обявления'  # новое имя которое будет заменять изначальное имя
