from django.urls import path, include
from django.contrib.auth import views as adminviews
from . import views

urlpatterns = [
    path('login/', adminviews.LoginView.as_view()),
    path('register/', views.register),
    # path('register/customer/', views.customer_register, name='customer_signup'),
    # path('register/administrator/', views.administrator_register, name='administrator_signup'),
]

# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
