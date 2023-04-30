from django.db import models


class Url(models.Model):
    original_link = models.URLField()
    shortened_link = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}: {self.original_link} - {self.shortened_link}"

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"
