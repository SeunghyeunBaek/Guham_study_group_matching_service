from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
