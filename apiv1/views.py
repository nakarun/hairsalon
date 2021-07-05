from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

from hairsalon.models import News
from pointcard.models import PointCard
from .serializers import NewsSerializer, PointCardSerializer


# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PointCardViewSet(viewsets.ModelViewSet):
    queryset = PointCard.objects.all()
    serializer_class = PointCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'
