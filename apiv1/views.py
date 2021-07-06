from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

from hairsalon.models import Salon, News
from pointcard.models import PointCard
from .serializers import SalonSerializer, NewsSerializer, PointCardSerializer


# Create your views here.

class SalonFilter(filters.FilterSet):
    """
    SalonStaff.uuidからSalonをretreiveするためのfilter
    """

    staff = filters.UUIDFilter(field_name='staffs')

    class Meta:
        model = Salon
        fields = '__all__'


class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SalonFilter


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
