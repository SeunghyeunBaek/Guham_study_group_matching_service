from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


# READ ALL
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


# Search
def search(request):
    study_place = request.POST.get('study_place')
    study_category = request.POST.get('study_category')
    study_time = request.POST.get('study_time')
    # raise()
    # 조건에 맞는 포스트 검색
    post_searched = Post.objects.filter(study_place=study_place).filter(study_category=study_category).filter(study_place=study_place)
    context = {
        'posts': post_searched,
    }
    return render(request, 'posts/index.html', context)


# READ ONE
def detail(request, post_id):
    post_selected = Post.objects.get(id=post_id)
    context = {
        'post_selected': post_selected,
    }
    return render(request, 'posts/detail.html', context)


@login_required
# CREATE
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
        else:
            pass
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)


# DELETE
def delete(request, post_id):
    post_selected = Post.objects.get(id=post_id)
    post_selected.delete()
    return redirect('posts:index')


# UPDATE
def update(request, post_id):
    post_selected = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post_selected)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post_id)
        else:
            pass
    else:
        form = PostForm(instance=post_selected)
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)
