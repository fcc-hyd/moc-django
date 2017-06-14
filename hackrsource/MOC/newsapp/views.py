from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from models import NewsArticle, NewsBookmark


# Create your views here.
def home(request):
    results = NewsArticle.objects.all()
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
        url_to_image = result.url_to_image
        published_at = result.published_at
        if published_at is None:
            published_at = ""
        source = result.source
        temp = [author, title, description, url, url_to_image, published_at, source]
        i = result.article_id
        d[i] = temp
    return render(request, 'newsapp/home.html', {'result': d})


def bookmark(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    user = User.objects.get(id=1)  # will be made dynamic once users login is added
    article = NewsArticle.objects.get(article_id=article_id)
    new_bookmark = NewsBookmark(user=user, article=article, bookmarked_at=datetime.now())
    new_bookmark.save()
    i = new_bookmark.bookmark_id
    return HttpResponse("Success bookmark id = " + str(i))


def unbookmark(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    article = NewsArticle.objects.get(article_id=article_id)
    NewsBookmark.objects.filter(article=article).delete()
    return HttpResponse("Success remove bookmark")


def profile(request):
    d = {}
    user = User.objects.get(id=1)
    result_set = NewsBookmark.objects.filter(user=user)
    for result in result_set:
        temp = [result.article.author, result.article.title, result.article.description, result.article.url,
                result.article.url_to_image, result.article.published_at, result.article.source]
        i = result.article.article_id
        d[i] = temp
    return render(request, 'newsapp/profile.html', {'result': d})
