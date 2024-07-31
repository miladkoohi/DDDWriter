from rest_framework import generics
from user.application.services import UserService
from user.presentation.serializers import UserSerializer
from user.infrastructure.repositories import DjangoUserRepository

user_service = UserService(DjangoUserRepository())

class UserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return user_service.find_all()

    def perform_create(self, serializer):
        user_service.create_user(serializer.validated_data['username'], serializer.validated_data['password'])
