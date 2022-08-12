from django.db import models

# Create your models here.

class User(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    author_profile = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    seconed_thumbnail = models.ImageField()
    overview = models.CharField(max_length=1000)
    brief_overview = models.CharField(max_length=1000)