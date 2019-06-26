from django.db import models
from django.conf import settings

STUDY_CATEGORY = [
    ('python', 'Python'),
    ('r', 'R'),
    ('c', 'C'),
    ('java', 'Java'),
]

STUDY_PLACE = [
    ('강남역', '강남역'),
    ('교대역', '교대역'),
    ('역삼역', '역삼역'),
]

STUDY_DAY = [
    ('주1회', '주1회'),
    ('주2회', '주2회'),
    ('주3회', '주3회'),
    ('협의', '협의'),
]

STUDY_TIME = [
    ('1hour', '1hour'),
    ('2hour', '2hour'),
    ('3hour', '3hour'),
]


class HashTag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class Post(models.Model):
    hash_tag = models.ManyToManyField(HashTag, blank=True, related_name='match_room_tagged')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    applicant = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='applied_post')
    title = models.CharField(max_length=50)
    study_category = models.CharField(max_length=10, choices=STUDY_CATEGORY)
    number_people = models.IntegerField()
    study_place = models.CharField(max_length=10, choices=STUDY_PLACE)
    study_day = models.CharField(max_length=10, choices=STUDY_DAY)
    study_time = models.CharField(max_length=10, choices=STUDY_TIME)
    content = models.TextField()
    hash_tag_list = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
