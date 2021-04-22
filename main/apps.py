from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.schedulers as cron
        cron.send_report()
