from blog.domain.entities import Article
from blog.domain.repositories import ArticleRepository

class ArticleService:
    def __init__(self, article_repository: ArticleRepository):
        self.article_repository = article_repository

    def create_article(self, title: str, content: str):
        article = Article(title, content)
        self.article_repository.save(article)
        return article

    def find_all(self):
        return self.article_repository.find_all()
