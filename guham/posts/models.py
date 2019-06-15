from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL  # user


class Post(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)

