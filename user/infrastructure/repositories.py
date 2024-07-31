from user.domain.repositories import UserRepository
from user.domain.entities import CustomUser

class DjangoUserRepository(UserRepository):
    def save(self, user):
        user.save()

    def find_by_id(self, user_id):
        return CustomUser.objects.get(id=user_id)

    def find_all(self):
        return CustomUser.objects.all()
