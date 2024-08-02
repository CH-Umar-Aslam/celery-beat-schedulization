from __future__ import absolute_import ,unicode_literals

import os
from celery import Celery
from django.conf import settings 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asynjobs.settings')
from celery.schedules import crontab
app = Celery('asynjobs')


app.conf.enable_utc=False
app.conf.update(timezone='Asia/Karachi')

app.conf.beat_schedule = {
    'fetch-every-10-seconds': {
        'task': 'bgapi.task.fetch_users',
        'schedule': 10.0,  # 5 seconds interval
    },
    'fetch-every-hour': {
        'task': 'bgapi.task.fetch_users',
        'schedule': crontab(minute=0, hour='*/1'),  # every hour
    },
}


app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
  print(f'Request :  {self.request!r}')
