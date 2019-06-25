from django.forms import ModelForm
from .models import MatchPost


class MatchPostForm(ModelForm):
    class Meta:
        model = MatchPost
        fields = [
            'category', 'place', 'content', 'hash_tag_list'
        ]
