from django.urls import include, path, re_path
from rest_framework import routers

from .endpoints import UrlListAPIView, CreateShortUrlAPIView, GetOriginalUrlAPIView


router = routers.SimpleRouter()
#router.register("url_viewset", UrlListAPIView)
#router.register("url_create", CreateShortUrlAPIView)
#router.register("url_get", GetOriginalUrlAPIView)


urlpatterns = [
    path("", include(router.urls)),
    path("url_viewset/", UrlListAPIView.as_view()),
    path("url_create/", CreateShortUrlAPIView.as_view()),
    path("url_get/", GetOriginalUrlAPIView.as_view()),
]
