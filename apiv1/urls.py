from django.urls import path, include
from rest_framework import routers

from .views import SalonViewSet, NewsViewSet, PointCardViewSet


router = routers.DefaultRouter()
router.register('salon', SalonViewSet)
router.register('news', NewsViewSet)
router.register('pointcard', PointCardViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]

