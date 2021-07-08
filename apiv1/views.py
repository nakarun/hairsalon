from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters

from hairsalon.models import Salon, News
from pointcard.models import PointCard, Stamp
from accounts.models import CustomerUser
from .serializers import SalonSerializer, NewsSerializer, PointCardSerializer, StampSerializer, CustomerUserSerializer


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

    def list(self, request, *args, **kwargs):
        """
        スタッフに対し紐付いているサロンは１つなのが基本なので、
        紐付いているサロンが１つであった場合はリストを返さずオブジェクトを返す
        """
        response = super().list(request, *args, **kwargs)
        if len(response.data) == 1:
            salon_uuid = response.data[0]['uuid']
            salon = get_object_or_404(Salon, pk=salon_uuid)
            serializer = SalonSerializer(instance=salon)
            return Response(serializer.data, status.HTTP_200_OK)
        return response


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


class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer
    permission_classes = [IsAuthenticated]
