from rest_framework import serializers
from .models import *

class tbl_MST_NewsArticleSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = tbl_MST_NewsArticle
		#fields = ('articleId', 'title')
		fields = '__all__'


class tbl_TRN_NewsCommentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = tbl_TRN_NewsComment
		fields = '__all__'
