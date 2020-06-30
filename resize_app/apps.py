from django.apps import AppConfig


class ResizeAppConfig(AppConfig):
    name = 'resize_app'

    def ready(self):
        import resize_app.signals
