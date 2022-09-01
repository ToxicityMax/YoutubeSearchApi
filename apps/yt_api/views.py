from django.shortcuts import render
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
# from .models import *

class TestView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        pass