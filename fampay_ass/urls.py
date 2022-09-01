import django.http
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


# from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_ROOT, STATIC_URL


def home(request: django.http.HttpRequest):
    return HttpResponse("Api server running")


schema_view = get_schema_view(
    openapi.Info(
        title="Fampay Assingment apis",
        default_version='v1',
        description="Documentation of currently available for FamPay Assingment",
    ),
    public=True,
    permission_classes=[AllowAny],
)
path('', home, name="HOME")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('search/', include('apps.yt_api.urls')),
    path('', home, name="HOME")
]

urlpatterns += [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
