from django.urls import path
from . import views

urlpatterns = [
    path('', views.waiting_room, name='waiting_room'),
    path('json/', views.rest_chat, name='rest_chat'),
    path('<str:room_name>/', views.chat, name='chat'),
]
