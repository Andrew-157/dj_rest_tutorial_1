from django.shortcuts import render
from .models import Language
from .serializers import LanguageSerializer
from rest_framework import viewsets


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
