from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def find_by_id(self, user_id):
        pass

    @abstractmethod
    def find_all(self):
        pass
