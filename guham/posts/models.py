from django.db import models
from django.conf import settings

# TODO from django.conf import settings

# TODO user = settings.AUTH_USER_MODEL  # user

STUDY_CATEGORY = [
    ('python', 'Python'),
    ('r', 'R'),
    ('java', 'Java'),
]

STUDY_PLACE = [
    ('강남', '강남역'),
    ('교대', '교대역'),
    ('역삼', '역삼역'),
]

STUDY_DAY = [
    ('주1회','주1회'),
    ('주2회','주2회'),
    ('주3회','주3회'),
    ('협의','협의'),
]

STUDY_TIME = [
    ('1hour', '1hour'),
    ('2hour', '2hour'),
    ('3hour', '3hour'),
]

class Post(models.Model):
    title = models.CharField(max_length=50)
    study_category = models.CharField(max_length=10, choices=STUDY_CATEGORY)
    number_people = models.IntegerField()
    study_place = models.CharField(max_length=10, choices=STUDY_PLACE)
    study_day = models.CharField(max_length=10, choices=STUDY_DAY)
    study_time = models.CharField(max_length=10, choices=STUDY_TIME)
    content = models.TextField()
    summary = models.TextField()

    # TODO user = models.ForeignKey(user, on_delete=models.CASCADE)