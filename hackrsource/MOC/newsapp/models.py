from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# will be using users class inbuilt in django

class NewsArticle(models.Model):
    article_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30, blank=True, default="")
    title = models.CharField(max_length=100, blank=True, default="")
    description = models.CharField(max_length=250, blank=True, default="")
    url = models.CharField(max_length=50, blank=True, default="")
    url_to_image = models.CharField(max_length=80, blank=True, default="")
    published_at = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=30, default="")

    def __unicode__(self):
        return str(self.article_id)


class NewsComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="article_comments")
    commented_at = models.DateField()

    class Meta:
        unique_together = ('user', 'article',)

    def __unicode__(self):
        return str(self.comment_id)


class NewsBookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookmark")
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="article_bookmark")
    bookmarked_at = models.DateField()

    class Meta:
        unique_together = ('user', 'article',)

    def __unicode__(self):
        return str(self.bookmark_id)


class NewsLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="article_likes")
    liked_at = models.DateField()

    class Meta:
        unique_together = ('user', 'article',)

    def __unicode__(self):
        return str(self.like_id)
