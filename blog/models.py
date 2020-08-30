from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms


class CV(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.CharField(default="Education", max_length=200, choices=[("About Me","About Me"),("Achievements","Achievements"),("Education", "Education"),("Work Experience","Work Experience")])
    title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField(default=timezone.now, blank=False, null=False)
    end_date = models.DateField(default=timezone.now(), blank=False, null=False)

    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    datetime = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.datetime = timezone.now()
        self.save()

    def __str__(self):
        return self.title
