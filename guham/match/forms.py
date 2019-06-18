from django.forms import ModelForm
from .models import MatchPost


class MatchPostForm(ModelForm):
    class Meta:
        model = MatchPost
        fields = [
            'study_category',
            'number_people',
            'study_place',
            'study_day',
            'study_time',
        ]


