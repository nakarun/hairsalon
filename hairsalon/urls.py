from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('news/<int:news_id>/', views.news_detail, name="news_detail"),
]