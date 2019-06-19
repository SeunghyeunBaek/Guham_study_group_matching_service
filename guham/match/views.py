from django.shortcuts import render, redirect
from .forms import MatchPostForm
from .models import MatchPost
from django.contrib.auth.decorators import login_required


@login_required
def set_conditions(request):
    if request.method == 'POST':
        form = MatchPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            context = {
                'form': form,
                'match_id' : form.id,
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



