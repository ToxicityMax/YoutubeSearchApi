from django.urls import path

from .views import (
    VideoPaginatedResponse,
    SearchView)

urlpatterns = [
    path('search/', SearchView.as_view()),
    path('', VideoPaginatedResponse.as_view())
]
