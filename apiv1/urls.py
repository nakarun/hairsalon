from django.urls import path, include
from rest_framework import routers

from .views import NewsViewSet


router = routers.DefaultRouter()
router.register('news', NewsViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]

