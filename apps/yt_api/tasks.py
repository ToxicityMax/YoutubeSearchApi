# from celery.schedules import crontab
from celery import shared_task

from fampay_ass.settings import KEYWORD as keyword
from .helpers import YoutubeApi
from .models import VideoDetails


@shared_task(name="update_db")
def update_db(message=None, *args, **kwargs):
    """Function which consumes YouTube data api for a keyword and storing new videos to database"""
    yapi = YoutubeApi(keyword=keyword)
    snippets = yapi.get_videos_by_keyword()
    new_vids = []
    for snippet in snippets:
        data = yapi.create_obj(snippet, keyword)
        if not VideoDetails.objects.filter(yt_id=data.get('yt_id')).exists():
            new_vids.append(data)
            print(data.get('yt_id'))
    VideoDetails.objects.bulk_create([VideoDetails(**data) for data in new_vids])
    print(f"Updated Database for {keyword}")
