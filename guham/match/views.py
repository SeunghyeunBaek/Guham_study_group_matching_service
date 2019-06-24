from django.shortcuts import render, redirect
from .forms import MatchPostForm
from .models import MatchPost, HashTag
from django.contrib.auth.decorators import login_required
from fuzzywuzzy import fuzz
from django.db.models import F
from django.contrib.postgres.search import TrigramSimilarity
# get matching score


@login_required
def set_conditions(request):
    if request.method == 'POST':
        form = MatchPostForm(request.POST)
        if form.is_valid():
            post_new = form.save(commit=False)
            post_new.user = request.user
            post_new.save()
            # 해시태그 추가
            content = form.cleaned_data.get('content')
            words = content.split()
            for word in words:
                if word[0] == '#':
                    hash_tag_new = HashTag.objects.get_or_create(content=word)
                    post_new.hash_tag.add(hash_tag_new[0])

            hash_tags = post_new.hash_tag.order_by('content').all()
            hash_tag_list = []
            for tag in hash_tags:
                hash_tag_list.append(tag.content)
            hash_tag_list = ''.join(hash_tag_list)

            post_new.hash_tag_list = hash_tag_list
            post_new.save()

            context = {
                'post_new': post_new,
            }
            return render(request, "match/detail.html", context)
        else:
            pass
    else:
        form = MatchPostForm()
    context = {
        'form': form
    }
    return render(request, 'match/set_conditions.html', context)


def matched_users(request, match_post_id):
    match_posts = MatchPost.objects.all()  # 모든 post
    my_post = MatchPost.objects.get(id=match_post_id)
    my_hash_tag = MatchPost.objects.get(id=match_post_id).hash_tag_list  # 내 hash_tag
    match_posts_sorted = sorted(match_posts, key=lambda match_post: match_post.score_hash_tag(my_hash_tag), reverse=True)
    context = {
        'my_post': my_post,
        'posts': match_posts_sorted
    }
    # 나의 해시태그를 문자열로 변경
    # my_hash_tag_list = []
    # for tag in my_hash_tag:
    #     my_hash_tag_list.append(tag.content)
    # my_hash_tag = ' '.join(my_hash_tag_list)

    # match_posts = MatchPost.objects.annotate(
    #     match_persent = fuzz.ratio("#apple", my_hash_tag)
    # ).order_by('match_persent')
    # print(match_posts)
    # tmp = MatchPost.objects.annotate(
    #     # match_persent = TrigramSimilarity('hash_tag_list', my_hash_tag)
    #     score=F('id')+1
    # )
    # print(tmp.score)
    #
    # context = {
    #     'my_post': my_post,
    # }
    return render(request, 'match/matched_users.html', context)


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



