from rest_framework import serializers
from news.models import *


class NewsArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    article_url = serializers.URLField(required=False)

    class Meta:
        model = NewsArticle
        fields = (
            'title',
            'description',
            'article_url',
        )
