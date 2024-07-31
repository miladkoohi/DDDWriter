from django.urls import path
from .views import ArticleListCreate

urlpatterns = [
    path('articles/', ArticleListCreate.as_view(), name='article-list-create'),
]
