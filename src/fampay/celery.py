import os

from celery import Celery

"""Usual stuff for celery"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')
app = Celery('fampay')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


"""Scheduling update_db function which runs every 10sec"""
app.conf.beat_schedule = {
    'background_job_for_yt': {
        'task': 'update_db',
        'schedule': 10.0,
        'args': ""
    },
}
