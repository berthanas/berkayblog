from rest_framework import serializers
from . import models


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'content', 'created_date')
        model = models.Article