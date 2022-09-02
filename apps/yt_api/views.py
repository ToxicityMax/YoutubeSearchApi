from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import pagination
from rest_framework import serializers
from rest_framework.permissions import AllowAny

from .models import VideoDetails


class StandardResultPagination(pagination.PageNumberPagination):
    """Standard Pagination class"""
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
    """GET api to fetch the latest videos details in paginated response ordered by reverse chronological order of their 
    publishing date """

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = VideoDetails
            fields = "__all__"
            ref_name = "Pagination response"

    permission_classes = [AllowAny]
    pagination_class = StandardResultPagination
    serializer_class = OutputSerializer

    def get_queryset(self):
        """Query set function used by pagination class"""
        keyword = self.request.GET.get('keyword', None)
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
    """Search api for getting results based on query(q)"""

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = VideoDetails
            fields = "__all__"
            ref_name = "Search Response"

    permission_classes = [AllowAny]
    serializer_class = OutputSerializer
    pagination_class = StandardResultPagination

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        return VideoDetails.objects.filter(Q(title__contains=q) | Q(description__contains=q)).all()
