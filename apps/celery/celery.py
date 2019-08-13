from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.dev')
app = Celery(main='django_sqs_example')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'display_time-30-seconds': {
        'task': 'apps.demoapp.tasks.display_time',
        'schedule': 10.0,
        'args': (1,2)
    },
}

"""
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10, my_task.s(66))

from django_celery_beat.models import PeriodicTask, IntervalSchedule

schedule= IntervalSchedule.objects.create(every=10, period=IntervalSchedule.SECONDS)
task = PeriodicTask.objects.create(interval=schedule, name='any name', task='tasks.my_task', args=json.dumps([66]))
"""

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

"""
-l debug
-l info

celery -A apps.celery worker -l debug
celery -A apps.celery worker -l info

celery -A apps.celery beat -l debug -S django_celery_beat.schedulers.DatabaseScheduler
"""
