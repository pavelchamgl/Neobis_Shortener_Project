from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
import pyshorteners

from .models import Url
from .serializers import UrlSerializer


class UrlListAPIView(ListAPIView):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    permission_classes = [permissions.AllowAny]


class CreateShortUrlAPIView(APIView):
    serializer_class = UrlSerializer

    def post(self, request, *args, **kwargs):
        original_link = request.POST["original_link"]
        url = pyshorteners.Shortener()
        shortened_link = url.tinyurl.short(original_link)
        new_link = Url.objects.create(original_link=original_link, shortened_link=shortened_link)
        serializer = self.serializer_class(new_link)
        return Response(serializer.data)


class GetOriginalUrlAPIView(APIView):
    serializer_class = UrlSerializer

    def get(self, request, *args, **kwargs):
        shortened_link = request.POST["shortened_link"]
        url = Url.objects.filter(shortened_link=shortened_link).first()
        serializer = self.serializer_class(url)
        return Response(serializer.data)
