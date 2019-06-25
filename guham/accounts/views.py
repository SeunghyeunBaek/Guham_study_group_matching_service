from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import User

def signup(request):
    # 로그인 됐을 때 다시 회원가입 하는 자들 방지
    if request.user.is_authenticated:
        return redirect('posts:index')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('posts:index')
            else:
                pass
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('posts:index')
            else:
                pass
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('posts:index')


def user_page(request, user_id):
    user_selected = User.objects.get(id=user_id)
    context = {
        'user_selected': user_selected,
    }
    return render(request, 'accounts/user_page.html', context)

# 장바구니에 사람 넣기


def pick(request, user_id):
    me = request.user  # 현재유저
    my_post = me.matchpost_set.first()
    you = User.objects.get(id=user_id)  # 장바구니에 넣으려는 유저
    # 나와 너가 다르다면!
    if me != you:
        if you in me.pick.all():  # 내가 너의 장바구니 안에 있다면
            me.pick.remove(you)
        else:
            me.pick.add(you)
    else:
        pass
    return redirect('match:matched_users', my_post.id)






