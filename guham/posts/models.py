from django.db import models
# TODO from django.conf import settings

# TODO user = settings.AUTH_USER_MODEL  # user

# TODO 수정했습니다.
class Post(models.Model):
    title = models.CharField(max_length=50)
    study_category = models.CharField(max_length=50, default='ALL')
    content = models.TextField()
    summary = models.TextField()
    # TODO user = models.ForeignKey(user, on_delete=models.CASCADE)