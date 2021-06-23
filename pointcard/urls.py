from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerPointCard.as_view(), name="pointcard"),
]