
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class ArticlesManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ArticlesManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    objects = ArticlesManager()
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
class CommentManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(CommentManager, self).filter(draft=False).filter(updated_at=timezone.now())

class Comment(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    article_id = models.PositiveIntegerField()
    content     = models.TextField()
    updated_at   = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()


    def __unicode__(self):  
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)
    class Meta:
        ordering = ['-updated_at']

