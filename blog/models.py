from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField(default=timezone.now, blank=False, null=False)
    end_date = models.DateField(default=timezone.now(), blank=False, null=False)

    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Item(models.Model):
    text = models.TextField(default='')