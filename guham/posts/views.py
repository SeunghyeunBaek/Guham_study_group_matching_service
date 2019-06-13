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
    pass


# CREATE
def create(request):
    if request.method == 'POST':
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
