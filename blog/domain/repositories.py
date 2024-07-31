from abc import ABC, abstractmethod

class ArticleRepository(ABC):
    @abstractmethod
    def save(self, article):
        pass

    @abstractmethod
    def find_by_id(self, article_id):
        pass

    @abstractmethod
    def find_all(self):
        pass
