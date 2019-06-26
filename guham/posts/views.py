from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post, HashTag
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator

from konlpy.tag import Okt  # 명사 추출
from sklearn.feature_extraction.text import TfidfVectorizer  # 벡터화
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도

okt = Okt()


# READ ALL
def index(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


# Search
def search(request):
    study_place = request.POST.get('study_place')
    study_category = request.POST.get('study_category')
    study_day = request.POST.get('study_day')
    query = request.POST.get('query')
    # 조건에 맞는 포스트 검색
    post_searched = Post.objects.filter(study_place=study_place,
                                        study_category=study_category,
                                        study_day=study_day,
                                        content__contains= query)
    paginator = Paginator(post_searched, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    post_searched = paginator.get_page(page)
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
            post_new = form.save(commit=False)
            post_new.user = request.user

            # 본문 토큰화
            content = form.cleaned_data.get('content')
            content_token = ','.join(okt.nouns(content))
            post_new.content_token = content_token
            post_new.save()

            # 해시태그 추가
            hash_tag_list = form.cleaned_data.get('hash_tag_list')
            words = hash_tag_list.split()
            for word in words:
                if word[0] == '#':
                    hash_tag_new = HashTag.objects.get_or_create(content=word)
                    post_new.hash_tag.add(hash_tag_new[0])

            # 해시태그 리스트 정렬
            hash_tag_list_new = []
            for hash in post_new.hash_tag.all():
                hash_tag_list_new.append(hash.content)
            hash_tag_list_new.sort()  # 정렬
            hash_tag_list_str = ' '.join(hash_tag_list_new)
            post_new.hash_tag_list = hash_tag_list_str
            post_new.save()

            context = {
                'post_new': post_new,
            }
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


def apply(request, post_id):
    me = request.user
    post = Post.objects.get(id=post_id)

    # 이미 지원한 스터디라면
    if post in me.applied_post.all():
        me.applied_post.remove(post)
        picked = False
    # 이전에 지원한 적 없다면
    else:
        me.applied_post.add(post)
        picked = True
    context = {
        'picked': picked,
    }
    return JsonResponse(context)


def test(request):
    return render(request, 'posts/test.html')
