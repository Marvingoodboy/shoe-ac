from django.apps import AppConfig


class DashoboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        import dashboard.signals
