from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters

from hairsalon.models import Salon, News
from pointcard.models import PointCard, Stamp
from accounts.models import SalonStaff, CustomerUser
from .serializers import SalonSerializer, NewsSerializer, PointCardSerializer, StampSerializer, SalonStaffSerializer, CustomerUserSerializer


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


class StampViewSet(viewsets.ModelViewSet):
    queryset = Stamp.objects.all()
    serializer_class = StampSerializer
    permission_classes = [IsAuthenticated]


class SalonStaffViewSet(viewsets.ModelViewSet):
    queryset = SalonStaff.objects.all()
    serializer_class = SalonStaffSerializer
    permission_classes = [IsAuthenticated]


class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    permission_classes = [IsAuthenticated]
