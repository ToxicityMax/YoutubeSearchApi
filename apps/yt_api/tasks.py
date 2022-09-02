from celery import shared_task, Celery
from celery.schedules import crontab

from .models import VideoDetails

@shared_task()
def print_objs():
    print("iasjdnsidjns")
