from django.apps import AppConfig

class GradingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pi1back.grading'

    def ready(self):
        import pi1back.grading.signals  # noqa
