from django.urls import path
from .views import register,user_login,calculate,user_logout



urlpatterns = [
    path('register', register, name='register'),
    path('', user_login, name='login'),
    path('calculate', calculate, name='calculate'),
    path('logout', user_logout, name='logout'),
    # path('login', LoginView.as_view(), name='login'),
    # path('logout', LogoutView.as_view(), name='logout'),
]