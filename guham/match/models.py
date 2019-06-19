# TODO 슬기 190618 models 수정

from django.db import models
from django.conf import settings

# Create your models here.

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


class MatchPost(models.Model):
    study_category = models.CharField(max_length=10, choices=STUDY_CATEGORY)  # 스터디 카테고리
    number_people = models.IntegerField()  # 인원수
    study_place = models.CharField(max_length=10, choices=STUDY_PLACE)  # 스터디 장소
    study_day = models.CharField(max_length=10, choices=STUDY_DAY)  # 주 n 회
    study_time = models.CharField(max_length=10, choices=STUDY_TIME)  # 시간

