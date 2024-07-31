from django.urls import path
from .views import UserListCreate

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
]
