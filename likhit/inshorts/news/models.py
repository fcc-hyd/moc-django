# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django_thumbs.db.models import ImageWithThumbsField

# Create your models here.

class NewsArticle(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    description = models.CharField(db_index=True, max_length=1000)
    article_url = models.URLField()
    article_thumbnail = ImageWithThumbsField(upload_to='images', sizes=((125, 125), (200, 200)))

    def __str__(self):
        return self.title
