from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from news import views

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
