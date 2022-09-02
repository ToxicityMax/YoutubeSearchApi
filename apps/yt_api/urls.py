from django.urls import path, include
from .views import (RegisterKeyword, VideoPaginatedResponse, SearchView)
from rest_framework import routers

urlpatterns = [
    path('keyword/', RegisterKeyword.as_view()),
    path('search/', SearchView.as_view()),
    path('', VideoPaginatedResponse.as_view())
    # path('/initiate',)
]
