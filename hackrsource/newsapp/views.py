from django.shortcuts import render
from django.http import HttpResponse
from newsparser.news_parser import NewsParser 
from .models import *
from .serializers import *
from django.shortcuts import render, redirect,get_object_or_404
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework import status


# list all News Articles or create a new one



class NewsArticleList(APIView):
	def get(self, request):
		articles = tbl_MST_NewsArticle.objects.all()
		serializer = tbl_MST_NewsArticleSerializer(articles , many=True)
		return Response(serializer.data)
	def post(self):
		pass

class CommentsList(APIView):
	def get(self, request):
		comments = tbl_TRN_NewsComment.objects.all()
		serializer = tbl_TRN_NewsCommentSerializer(comments , many=True)
		return Response(serializer.data)
	def post(self):
		pass
def home(request):
	#np = NewsParser()
	#results = np.parse()
	results = tbl_MST_NewsArticle.objects.all()
	#comments = tbl_TRN_NewsComment.all()
	d = {}
	i = 0
	for result in results:
		author = result.author
		if author is None:
			author = ""
		title = result.title
		if title is None:
			title = ""
		description = result.description
		if description is None:
			description = ""
		url = result.url
		urlToImage = result.urlToImage
		publishedAt = result.publishedAt
		if publishedAt is None:
			publishedAt = ""
		source = result.source
		temp = [author, title, description, url, urlToImage, publishedAt, source]
		d[i] = temp
		i += 1
	return render(request, 'newsapp/home.html', {'result':d})

def profile(request):
	pass
