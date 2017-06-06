from __future__ import unicode_literals

from django.db import models

# Create your models here.
# will be using users class inbuilt in django

class tbl_MST_NewsArticle(models.Model):
	articleId = models.AutoField(primary_key=True)
	author = models.CharField(max_length = 30)
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	url = models.CharField(max_length = 50)
	urlToImage = models.CharField(max_length = 80)
	publishedAt = models.DateField()

	def __str__(self):
		return(title)