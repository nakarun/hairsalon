from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('news/<int:news_id>/', views.NewsDetailView.as_view(), name="news_detail"),
]