from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User
from django.http import JsonResponse


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


@login_required
def update(request, user_id):
    user_selected = User.objects.get(id=user_id)
    if request.user == user_selected:  # 로그인 한 사람과 수정하려는 사람이 같을 때
        if request.method == 'POST':
            form = CustomUserChangeForm(data=request.POST, files=request.FILES, instance=user_selected)
            if form.is_valid():
                form.save()
                return redirect('accounts:user_page', user_id)
            else:
                pass
        else:
            form = CustomUserChangeForm(instance=user_selected)
        context = {
            'form': form,
            'user_selected': user_selected,
        }
        return render(request, 'accounts/update.html', context)
    else:
        # 로그인 한 사람과 수정하려는 사람이 같지 않을 경우 index 페이지 리턴
        return redirect('accounts:user_page', user_id)


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
            picked = False
        else:
            me.pick.add(you)
            picked = True
    else:
        pass
    # javascript로 변수 전달
    context = {
        'picked': picked,
    }
    return JsonResponse(context)


def clean(request, user_id):
    user_selected = User.objects.get(id=user_id)
    user_selected.pick.clear()
    return redirect('accounts:user_page', user_id)
