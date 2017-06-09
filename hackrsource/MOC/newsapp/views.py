from django.shortcuts import render
from django.http import HttpResponse
from newsparser.news_parser import NewsParser 
from models import tbl_MST_NewsArticle, tbl_TRN_NewsBookmark
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.
def home(request):
	results = tbl_MST_NewsArticle.objects.all()
	d = {}
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
		i = result.articleId
		d[i] = temp		
	return render(request, 'newsapp/home.html', {'result':d})

def bookmark(request):
	articleId = request.GET.get('id', None)
	articleID = int(articleId)
	user = User.objects.get(id = 1) #will be made dynamic once users login is added
	article = tbl_MST_NewsArticle.objects.get(articleId = articleID)
	newBookmark = tbl_TRN_NewsBookmark(userId = user, articleId=article, bookmarkedAt = datetime.now())
	newBookmark.save()
	print newBookmark
	i = newBookmark.bookmarkId
	return HttpResponse("Success with bookmark id = " + str(i))

def profile(request):
	pass