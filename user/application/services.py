from user.domain.entities import CustomUser
from user.domain.repositories import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, password: str):
        user = CustomUser(username=username)
        user.set_password(password)
        self.user_repository.save(user)
        return user

    def find_all(self):
        return self.user_repository.find_all()
