from rest_framework import serializers
from blog.infrastructure.models import ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'
