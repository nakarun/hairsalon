from django.urls import path
from . import views

urlpatterns = [
    path('', views.PointCardView.as_view(), name="pointcard"),
]