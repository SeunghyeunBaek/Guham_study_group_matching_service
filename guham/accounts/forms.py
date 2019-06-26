from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class CustomUserChangeForm(UserChangeForm):
    password = None  # 비밀번호 칸 제거

    class Meta:
        model = User
        fields = ['username', 'introduce', 'image']
