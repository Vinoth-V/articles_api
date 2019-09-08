from django.conf.urls import include
from rest_framework import routers
from django.conf.urls import url

from .views import (
    ArticleViewSet,
    ArticleDetailsViewSet,
    CommentDetailsViewSet
    )

urlpatterns = [
			url(r'^$', ArticleViewSet.as_view(), name='list and Create Articles'),
		    url(r'^(?P<pk>\d+)/$', ArticleDetailsViewSet.as_view(), name='Article Details'),
		    url(r'^(?P<article_id>\d+)/comments/$', CommentDetailsViewSet.as_view(), name='Article comments list')
			]