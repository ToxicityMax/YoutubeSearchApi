from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import pagination
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from fampay_ass.helpers import respond
from fampay_ass.settings import KEYWORD
from .helpers import YoutubeApi
from .models import VideoDetails
from .tasks import print_objs


class StandardResultPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('keyword', openapi.IN_QUERY, description="Keyword to get results",
                              type=openapi.TYPE_STRING, required=True)
        ]
    )
)
class VideoPaginatedResponse(generics.ListAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = VideoDetails
            fields = "__all__"
            ref_name = "Pagination response"

    permission_classes = [AllowAny]
    pagination_class = StandardResultPagination
    serializer_class = OutputSerializer

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', None)
        print_objs.delay()
        return VideoDetails.objects.filter(keyword=keyword).order_by('-published_at').all()


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, description="Query String for searching",
                              type=openapi.TYPE_STRING, required=True)
        ]
    )
)
class SearchView(generics.ListAPIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = VideoDetails
            fields = "__all__"
            ref_name = "Search Response"

    permission_classes = [AllowAny]
    serializer_class = OutputSerializer

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        return VideoDetails.objects.filter(Q(title__contains=q) | Q(description__contains=q)).all()


class RegisterKeyword(APIView):
    permission_classes = [AllowAny]

    def create_obj(self, snippet, keyword: str):
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

    def post(self, request):
        yapi = YoutubeApi(keyword=KEYWORD)
        snippets = yapi.get_videos_by_keyword()
        new_vids = []
        for snippet in snippets:
            data = self.create_obj(snippet, KEYWORD)
            if not VideoDetails.objects.filter(yt_id=data.get('yt_id')).exists():
                new_vids.append(data)
                print(data.get('yt_id'))
        VideoDetails.objects.bulk_create([VideoDetails(**data) for data in new_vids])
        return respond(200, "Success", snippets)
