from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'study_category',
            'number_people',
            'study_place',
            'study_day',
            'study_time',
            'content',
            'hash_tag_list',
        ]


