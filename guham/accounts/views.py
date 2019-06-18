from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
    # 로그인 됐을 때 다시 회원가입 하는 자들 방지
    if request.user.is_authencated:
        return redirect('posts:index')
    else:
        if request.method == 'POST':
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('posts:index')
            else:
                pass
        else:
            form = UserCreationForm()
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

