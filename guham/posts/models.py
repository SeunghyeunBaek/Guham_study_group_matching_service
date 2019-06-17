from django.db import models
# TODO from django.conf import settings

# TODO user = settings.AUTH_USER_MODEL  # user


class Post(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    # TODO user = models.ForeignKey(user, on_delete=models.CASCADE)