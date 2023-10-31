from __future__ import absolute_import

import os
import time

from django.conf import settings

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picasso_test.settings')

app = Celery('picasso_test')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(5)
    print('hello from debug_task')

