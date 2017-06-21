from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from models import NewsArticle, NewsBookmark, NewsLike
from forms import LoginForm, RegisterationForm, PasswordReset


# Create your views here.
def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home")
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            username = data["user"]
            password = data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/home")
            else:
                return HttpResponse("Error with login")
        else:
            return HttpResponse("The form is not valid")
    else:
        login_form = LoginForm()
        return render(request, 'newsapp/login.html', {'form': login_form})


def password_reset(request):
    password_reset_form = PasswordReset()
    return render(request, "newsapp/password_reset.html", {'form': password_reset_form})


def registeration(request):
    if request.method == "POST":
        register_form = RegisterationForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            username = data["user"]
            password = data["password"]
            email = data["email"]
            user = User.objects.create_user(username=username, password=password, email=email)
            if user is not None:
                user.save()
                login(request, user)
                return HttpResponseRedirect("/home")
            else:
                return HttpResponse("Error in creating the user object")
    else:
        register_form = RegisterationForm()
        return render(request, 'newsapp/register.html', {'form': register_form})


@login_required(login_url="/")
def home(request):
    results = NewsArticle.objects.all()
    d = {}
    user = request.user
    for result in results:
        liked = 1
        bookmarked = 1
        liked_result = NewsLike.objects.filter(article=result, user=user)
        bookmarked_result = NewsBookmark.objects.filter(article=result, user=user)
        if len(liked_result) == 0:
            liked = 0
        if len(bookmarked_result) == 0:
            bookmarked = 0
        temp = [result.author, result.title, result.description, result.url, result.url_to_image, result.published_at,
                result.source, liked, bookmarked]
        i = result.article_id
        d[i] = temp
    return render(request, 'newsapp/home.html', {'result': d})


@login_required(login_url="/")
def bookmark(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    user = request.user
    article = NewsArticle.objects.get(article_id=article_id)
    new_bookmark = NewsBookmark(user=user, article=article, bookmarked_at=datetime.now())
    new_bookmark.save()
    i = new_bookmark.bookmark_id
    return HttpResponse("Success bookmark id = " + str(i))


@login_required(login_url="/")
def unbookmark(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    article = NewsArticle.objects.get(article_id=article_id)
    user = request.user
    NewsBookmark.objects.filter(article=article, user=user).delete()
    return HttpResponse("Success remove bookmark")


@login_required(login_url="/")
def like(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    user = request.user
    article = NewsArticle.objects.get(article_id=article_id)
    new_like = NewsLike(user=user, article=article, liked_at=datetime.now())
    new_like.save()
    i = new_like.like_id
    return HttpResponse("Success bookmark id = " + str(i))


@login_required(login_url="/")
def unlike(request):
    article_id = request.GET.get('id', None)
    article_id = int(article_id)
    article = NewsArticle.objects.get(article_id=article_id)
    user = request.user
    NewsLike.objects.filter(article=article, user=user).delete()
    return HttpResponse("Success remove like")


@login_required(login_url="/")
def profile(request):
    d = {}
    user = request.user
    result_set = NewsBookmark.objects.filter(user=user)
    for result in result_set:
        liked = 1
        liked_result = NewsLike.objects.filter(article=result.article, user=user)
        if len(liked_result) == 0:
            liked = 0
        temp = [result.article.author, result.article.title, result.article.description, result.article.url,
                result.article.url_to_image, result.article.published_at, result.article.source, liked]
        i = result.article.article_id
        d[i] = temp
    return render(request, 'newsapp/profile.html', {'result': d})


@login_required(login_url="/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
