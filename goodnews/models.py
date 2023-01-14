from django.db import models


# Create your models here.

class Ad(models.Model):
    ad_img = models.ImageField()


class Event(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)
