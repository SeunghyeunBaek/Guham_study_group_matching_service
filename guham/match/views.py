from django.shortcuts import render, redirect
from .forms import MatchPostForm
from .models import MatchPost, HashTag
from django.contrib.auth.decorators import login_required

from konlpy.tag import Okt  # 명사 추출
from sklearn.feature_extraction.text import TfidfVectorizer  # 벡터화
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도
from django.core.paginator import Paginator

import re

from fuzzywuzzy import fuzz
from django.db.models import F
from django.contrib.postgres.search import TrigramSimilarity

# get matching score

okt = Okt()


@login_required
def set_conditions(request):
    if request.method == 'POST':
        form = MatchPostForm(request.POST)
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
            return redirect("match:matched_users", post_new.id)
        else:
            pass
    else:
        form = MatchPostForm()
    context = {
        'form': form
    }
    return render(request, 'match/set_conditions.html', context)


def matched_users(request, match_post_id):
    my_post = MatchPost.objects.get(id=match_post_id)
    category_selected = my_post.category
    place_selected = my_post.place

    match_posts = MatchPost.objects.filter(category=category_selected, place=place_selected)

    my_post = MatchPost.objects.get(id=match_post_id)
    my_hash_tag = my_post.hash_tag_list  # 내 hash_tag
    my_content_token = MatchPost.objects.get(id=match_post_id).content_token  # 내 content_token

    # get doc similarity
    corpus = []
    ids = []
    for match_post in match_posts:
        corpus.append(match_post.content_token)
        ids.append(match_post.id)
    post2corpus = dict(zip(ids, range(len(corpus))))
    tfidf_obj = TfidfVectorizer()
    tfidf_mat = tfidf_obj.fit_transform(corpus)
    sim_mat = cosine_similarity(tfidf_mat)
    # 더러운 코딩 가즈아
    match_posts_sorted = sorted(match_posts,
                                key=lambda post: (.8 * post.score_hash_tag(my_hash_tag) + .2 * 100 * sim_mat[
                                    post2corpus.get(match_post_id), post2corpus.get(post.id)]),
                                reverse=True)
    paginator = Paginator(match_posts_sorted, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'my_post': my_post,
        'posts': posts,
    }
    return render(request, 'match/matched_users.html', context)


def detail(request, match_post_id):
    post_selected = MatchPost.objects.get(id=match_post_id)
    context = {
        'post_selected': post_selected,
    }
    return render(request, 'match/detail.html', context)


def hash_tagged_posts(request, match_post_id, hash_tag_id):
    my_post = MatchPost.objects.get(id=match_post_id)
    hash_tag_selected = HashTag.objects.get(id=hash_tag_id)
    match_posts_tagged = hash_tag_selected.match_post_tagged.all()
    context = {
        'my_post': my_post,
        'posts': match_posts_tagged,
    }
    return render(request, 'match/matched_users.html', context)
# get dummies


# def detail(request, match_id):
#     match_post_selected = MatchPost.objects.get(id=match_id)
#     context = {
#         'match_post_selected': match_post_selected,
#     }
#     return render(request, 'match/detail.html', context)
# #
# def start(request, match_id):
#     form = MatchPost.objects.get(id=match_id)
#     context = {
#         'form':form,
#         'match_id':match_id,
#     }
#     return render(request, 'match/start.html', context)
#
# def success(request, user_id, match_id):
#     form = MatchPost.objects.get(id=match_id)
#     context = {
#         'form': form,
#         'match_id': form.id,
#     }
#     return render(request, 'match/success.html', context)
#
# def accept(request):
#
#     # 승낙 시 그룹 채팅방으로 이동
#     pass
