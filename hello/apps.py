from django.apps import AppConfig


class HelloConfig(AppConfig):
    import viewcomponents.button.button
    # def ready(Self):
    #     import hello.components.example
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'


