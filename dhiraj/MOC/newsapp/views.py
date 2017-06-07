from django.shortcuts import render
from django.http import HttpResponse
from newsparser.news_parser import NewsParser 
from models import tbl_MST_NewsArticle

# Create your views here.
def home(request):
	#np = NewsParser()
	#results = np.parse()
	results = tbl_MST_NewsArticle.objects.all()
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