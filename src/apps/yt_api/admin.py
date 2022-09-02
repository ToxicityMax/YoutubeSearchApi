# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import VideoDetails


@admin.register(VideoDetails)
class VideoDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'yt_id',
        'keyword',
        'thumbnail',
        'title',
        'description',
        'channel_id',
        'channel_title',
        'published_at',
        'created_at',
        'updated_at',
    )
    list_filter = ('published_at', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
