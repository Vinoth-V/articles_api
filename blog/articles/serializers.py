from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )


from articles.models import (Article,Comment)
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    # url = article_detail_url
    author = SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id','title','body','author']
        read_only_fields = [
            'id',
            'author',
        ]
    def get_author(self,obj):
        return str(obj.author.username)


class ArticleSaveSerializer(serializers.ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Article
        fields = ['id','title','body','author']
        read_only_fields = [
            'id',
            'author',
        ]

    def get_author(self,obj):
        return str(obj.author.username)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','article_id','updated_at']

    
class CommentSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','updated_at'] 
