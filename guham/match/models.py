from django.db import models
from django.conf import settings
from fuzzywuzzy import fuzz
from sklearn.metrics.pairwise import cosine_similarity

# Create your models here.

STUDY_CATEGORY = [
    ('python', 'python'),
    ('r', 'r'),
    ('c', 'c'),
    ('java', 'java'),
]

STUDY_PLACE = [
    ('강남역', '강남역'),
    ('교대역', '교대역'),
    ('역삼역', '역삼역'),
]

# STUDY_DAY = [
#     ('주1회','주1회'),
#     ('주2회','주2회'),
#     ('주3회','주3회'),
#     ('협의','협의'),
# ]

STUDY_TIME = [
    ('1hour', '1hour'),
    ('2hour', '2hour'),
    ('3hour', '3hour'),
]


# 해시태그
class HashTag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class MatchPost(models.Model):
    # 카테고리, 장소, 본문, 해시태그
    hash_tag = models.ManyToManyField(HashTag, blank=True, related_name='match_post_tagged')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')
    category = models.CharField(max_length=10, choices=STUDY_CATEGORY)  # 스터디 카테고리
    place = models.CharField(max_length=10, choices=STUDY_PLACE)  # 스터디 장소
    content = models.TextField()  # 본문
    content_token = models.TextField()  # 토큰화-명사 추출 된 본문
    hash_tag_list = models.TextField(blank=True)

    # 상대방의 해시태그와 나의 해시태그를 비교
    def score_hash_tag(self, ur_hash_tag_list):
        score = fuzz.ratio(self.hash_tag_list, ur_hash_tag_list)
        return .01 * score
