from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('map/', views.MapView.as_view(), name='map'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name="news_detail"),
]