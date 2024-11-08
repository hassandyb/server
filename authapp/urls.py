
# authapp/urls.py
from django.urls import path
from .views import register, user_login, user_logout, get_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user/', get_user, name='get_user'),
]
