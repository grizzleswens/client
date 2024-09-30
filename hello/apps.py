from django.apps import AppConfig


class HelloConfig(AppConfig):
    import viewcomponents.button.button
    import viewcomponents.form.form
    # def ready(Self):
    #     import hello.components.example
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'


