from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomerLogin.as_view(), name="customer_login"),
    path('signup/', views.CustomerSignUp.as_view(), name="customer_signup"),
    path('logout/', views.CustomerLogout.as_view(), name="customer_logout"),
    path('pointcard/', views.CustomerPointCard.as_view(), name="customer_pointcard"),
]