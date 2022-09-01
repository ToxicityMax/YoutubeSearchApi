import requests

from fampay_ass.settings import GAPI_KEY, KEYWORD


class YoutubeApi:
    URL = "https://youtube.googleapis.com/youtube/v3/search"
    API_KEY = GAPI_KEY
    KEYWORD = KEYWORD

    def request_yt(self, params):
        params['key'] = self.API_KEY
        return requests.get(self.URL, params=params).json()
