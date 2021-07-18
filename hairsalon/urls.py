from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('greeting/', views.GreetingView.as_view(), name='greeting'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('stylist/', views.StylistView.as_view(), name='stylist'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name="news_detail"),
    path('map/', views.MapView.as_view(), name='map'),
]