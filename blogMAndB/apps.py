from django.apps import AppConfig


class BlogmandbConfig(AppConfig):
    name = 'blogMAndB'

    def ready(self):
        import blogMAndB.signals

