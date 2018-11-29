from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:product_id>/', views.products_detail, name='products_detail'),
]
