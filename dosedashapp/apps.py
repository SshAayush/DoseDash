from django.apps import AppConfig
from django_cron import CronJobManager


class DosedashappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dosedashapp'

    # def ready(self):
    #     # Register the cron job
    #     CronJobManager.register(MyCronJob)