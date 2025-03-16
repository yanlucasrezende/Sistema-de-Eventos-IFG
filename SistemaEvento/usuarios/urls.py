from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('criar-usuario/', UserCreateView.as_view(), name='user_create'),
]