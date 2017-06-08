from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
# will be using users class inbuilt in django

class tbl_MST_NewsArticle(models.Model):
	articleId = models.AutoField(primary_key=True)
	author = models.CharField(max_length = 30, null=True)
	title = models.CharField(max_length = 100, null=True)
	description = models.CharField(max_length = 250, null=True)
	url = models.CharField(max_length = 50, null=True)
	urlToImage = models.CharField(max_length = 80, null=True)
	publishedAt = models.DateField(null=True)
	source = models.CharField(max_length = 30, default="")

	def __str__(self):
		return(title)


class tbl_TRN_NewsComment(models.Model):
	commentId = models.AutoField(primary_key = True)
	comment = models.CharField(max_length = 200)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)	
	articleId = models.ForeignKey(tbl_MST_NewsArticle, on_delete=models.CASCADE)
	commentedAt = models.DateField()

	def __str__(self):
		return(comment)

class tbl_TRN_NewsBookmark(models.Model):
	bookmarkId = models.AutoField(primary_key = True)
	userId = models.ForeignKey(User, on_delete=models.CASCADE)	
	articleId = models.ForeignKey(tbl_MST_NewsArticle, on_delete=models.CASCADE)
	bookmarkedAt = models.DateField()

	def __str__(self):
		return(str(articleId))

class tbl_TRN_NewsLike(models.Model):
	likeId = models.AutoField(primary_key = True)
	like = models.IntegerField()
	userId = models.ForeignKey(User, on_delete=models.CASCADE)	
	articleId = models.ForeignKey(tbl_MST_NewsArticle, on_delete=models.CASCADE)
	likedAt = models.DateField

	def __str__(self):
		return(str(articleId))