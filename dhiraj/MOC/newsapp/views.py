from django.shortcuts import render
from django.http import HttpResponse
from newsparser.news_parser import NewsParser 

# Create your views here.
def home(request):
	np = NewsParser()
	results = np.parse()
	i = 0
	d = {}
	for result in results:
		d[i] = result
		i += 1 
	return render(request, 'newsapp/home.html', {'result':d})