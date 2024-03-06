from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoseDash.settings')


app = Celery('DoseDash')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-reminder-every-day-at-5pm': {
        'task': 'dosedashapp.tasks.sendReminder',
        'schedule': crontab(hour=17, minute=0),
        # 'schedule': crontab(minute='*'),
    },
}