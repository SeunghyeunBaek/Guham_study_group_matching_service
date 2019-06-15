from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


# READ ALL
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


# READ ONE
def detail(request, post_id):
    post_selected = Post.objects.get(id=post_id)
    context = {
        'post_selected': post_selected,
    }
    return render(request, 'posts/detail.html', context)


# CREATE
def create(request):
    if request.method == 'POST':
        raise()
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
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


