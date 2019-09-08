from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from articles.serializers import (
	ArticleSerializer,
	ArticleSaveSerializer,
    CommentSerializer,
    CommentSaveSerializer
	)

from rest_framework.mixins import (
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin, 
    UpdateModelMixin
    )

from django.contrib.auth import get_user_model

from .pagination import (ArticleSetPagination, ArticlePageNumberPagination)

from rest_framework import filters

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

User = get_user_model()
from .permissions import IsAuthorOrAdmin

from articles.models import (Article,Comment)


class ArticleViewSet(RetrieveModelMixin, CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    pagination_class = ArticlePageNumberPagination
    queryset = Article.objects.all().order_by('author__username')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetailsViewSet(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    permission_classes = [IsAuthorOrAdmin]
    queryset = Article.objects.all()
    serializer_class=ArticleSaveSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentDetailsViewSet(RetrieveModelMixin, CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSaveSerializer
    pagination_class = ArticlePageNumberPagination

    lookup_field = 'article_id'
    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects.all().filter(article_id=article_id)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        article_id = self.kwargs['article_id']
        serializer.save(article_id=article_id)