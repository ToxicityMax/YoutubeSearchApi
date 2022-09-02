import requests

from fampay_ass.settings import GAPI_KEYS


class YoutubeApi:
    URL = "https://youtube.googleapis.com/youtube/v3/search"
    API_KEYS = GAPI_KEYS
    KEYWORD = ""
    CURRENT_KEY = None

    def __init__(self, keyword=''):
        self.KEYWORD = keyword
        self.CURRENT_KEY = GAPI_KEYS[0]

    def request_yt(self, params):
        params['key'] = self.CURRENT_KEY
        return requests.get(self.URL, params=params).json()

    def get_videos_by_keyword(self) -> list:
        params = {
            "q": self.KEYWORD,
            "part": "snippet",
            "maxResults": "50",
            "order": "date",
            "key": self.KEYWORD
        }
        return self.request_yt(params=params)['items']
