from secrets import choice

import requests

from fampay.settings import GAPI_KEYS


class YoutubeApi:
    """Generic class for sending request to Youtube search api for a keyword with multiple apiKeys"""
    URL = "https://youtube.googleapis.com/youtube/v3/search"
    API_KEYS = GAPI_KEYS
    KEYWORD = ""
    COUNTER = 0

    def __init__(self, keyword='') -> None:
        self.KEYWORD = keyword

    def request_yt(self, params) -> dict | None:
        """Makes request and handles expired keys"""
        params['key'] = choice(self.API_KEYS)
        response = requests.get(self.URL, params=params)
        if response.status_code == 403:
            if self.COUNTER < 10:
                self.COUNTER += 1
                return None
            else:
                raise Exception("All api keys are expired")
        else:
            return response.json()

    def get_videos_by_keyword(self) -> list:
        """Sets the params and calls request function"""
        params = {
            "q": self.KEYWORD,
            "part": "snippet",
            "maxResults": "50",
            "order": "date",
            "key": self.KEYWORD
        }
        response = None
        while not response:
            response = self.request_yt(params=params)
        return response['items']

    def create_obj(self, snippet, keyword: str) -> dict:
        """Created object for storing in db"""
        return {
            "yt_id": snippet['id']['videoId'],
            "keyword": keyword,
            "title": snippet['snippet']['title'],
            "description": snippet['snippet']['description'],
            "channel_id": snippet['snippet']['channelId'],
            "channel_title": snippet['snippet']['channelTitle'],
            "published_at": snippet['snippet']['publishedAt'],
            "thumbnail": snippet['snippet']['thumbnails']['high']['url']
        }
