from django.urls import path, include
from rest_framework import routers

from .views import SalonViewSet, NewsViewSet, PointCardViewSet, StampViewSet, SalonStaffViewSet, CustomerUserViewSet


router = routers.DefaultRouter()
router.register('salon', SalonViewSet)
router.register('news', NewsViewSet)
router.register('pointcard', PointCardViewSet)
router.register('stamp', StampViewSet)
router.register('staff', SalonStaffViewSet)
router.register('customer', CustomerUserViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]

