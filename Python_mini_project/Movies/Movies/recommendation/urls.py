from django.urls import path
from . import views

urlpatterns = [
    path('', views.startPage, name='startPage'),
    path('mainPage/', views.mainPage, name='mainPage'),
    path('recommendations/', views.get_recommendations, name='recommendations'),
]