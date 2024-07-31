from blog.domain.repositories import ArticleRepository
from blog.infrastructure.models import ArticleModel

class DjangoArticleRepository(ArticleRepository):
    def save(self, article):
        article_model = ArticleModel(title=article.title, content=article.content)
        article_model.save()

    def find_by_id(self, article_id):
        return ArticleModel.objects.get(id=article_id)

    def find_all(self):
        return ArticleModel.objects.all()
