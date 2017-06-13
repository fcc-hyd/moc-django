from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


# Create your models here.
# will be using users class inbuilt in django

class NewsArticle(models.Model):
    article_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True)
    url = models.CharField(max_length=50, null=True)
    url_to_image = models.CharField(max_length=80, null=True)
    published_at = models.DateField(null=True)
    source = models.CharField(max_length=30, default="")

    def __str__(self):
        return str(self.articleId)


class NewsComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    commented_at = models.DateField()

    def __str__(self):
        return str(self.commentId)

    class Meta:
        unique_together = ('user', 'article',)


class NewsBookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    bookmarked_at = models.DateField()

    def __str__(self):
        return str(self.bookmarkId)

    class Meta:
        unique_together = ('user', 'article',)


class NewsLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    like = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    liked_at = models.DateField

    def __str__(self):
        return str(self.likeId)

    class Meta:
        unique_together = ('user', 'article',)
