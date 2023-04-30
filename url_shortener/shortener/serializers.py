from rest_framework.serializers import ModelSerializer

from .models import Url


class UrlSerializer(ModelSerializer):
    class Meta:
        model = Url
        fields = ["original_link", "shortened_link"]
