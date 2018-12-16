from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sort/<str:category>/', views.category, name='category'),
]
