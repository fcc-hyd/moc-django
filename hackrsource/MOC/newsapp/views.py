from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from models import NewsArticle, NewsBookmark
from forms import LoginForm, RegisterationForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            username = data["user"]
            password = data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                results = NewsArticle.objects.all()
                d = {}
                for result in results:
                    temp = [result.author, result.title, result.description, result.url, result.url_to_image,
                            result.published_at,
                            result.source]
                    i = result.article_id
                    d[i] = temp
                return render(request, 'newsapp/home.html', {'result': d})
            else:
                return HttpResponse("Error with login")
        else:
            return HttpResponse("The form is not valid")
    else:
        login_form = LoginForm()
        return render(request, 'newsapp/login.html', {'form': login_form})


def registeration(request):
    if request.method == "POST":
        register_form = RegisterationForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            username = data["user"]
            password = data["password"]
            email = data["email"]
            user = User(username = username, password = password, email = email)
            if user is not None:
                user.save()
                login(request, user)
                results = NewsArticle.objects.all()
                d = {}
                for result in results:
                    temp = [result.author, result.title, result.description, result.url, result.url_to_image,
                            result.published_at,
                            result.source]
                    i = result.article_id
                    d[i] = temp
                return render(request, 'newsapp/home.html', {'result': d})
            else:
                return HttpResponse("Error in creating the user object")
    else:
        register_form = RegisterationForm()
        return render(request, 'newsapp/register.html', {'form': register_form})


@login_required
def home(request):
    results = NewsArticle.objects.all()
    d = {}
    for result in results:
        temp = [result.author, result.title, result.description, result.url, result.url_to_image, result.published_at,
                result.source]
        i = result.article_id
        d[i] = temp
    return render(request, 'newsapp/home.html', {'result': d})

@login_required
def bookmark(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    user = request.user
    article = NewsArticle.objects.get(article_id=article_id)
    new_bookmark = NewsBookmark(user=user, article=article, bookmarked_at=datetime.now())
    new_bookmark.save()
    i = new_bookmark.bookmark_id
    return HttpResponse("Success bookmark id = " + str(i))

@login_required
def unbookmark(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    article = NewsArticle.objects.get(article_id=article_id)
    NewsBookmark.objects.filter(article=article).delete()
    return HttpResponse("Success remove bookmark")

@login_required
def like(request):
    pass

@login_required
def unlike(request):
    pass

@login_required
def profile(request):
    d = {}
    user = request.user
    result_set = NewsBookmark.objects.filter(user=user)
    for result in result_set:
        temp = [result.article.author, result.article.title, result.article.description, result.article.url,
                result.article.url_to_image, result.article.published_at, result.article.source]
        i = result.article.article_id
        d[i] = temp
    return render(request, 'newsapp/profile.html', {'result': d})
