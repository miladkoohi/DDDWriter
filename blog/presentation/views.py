from rest_framework import generics
from blog.application.services import ArticleService
from blog.presentation.serializers import ArticleSerializer
from blog.infrastructure.repositories import DjangoArticleRepository

article_service = ArticleService(DjangoArticleRepository())

class ArticleListCreate(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return article_service.find_all()

    def perform_create(self, serializer):
        article_service.create_article(serializer.validated_data['title'], serializer.validated_data['content'])
