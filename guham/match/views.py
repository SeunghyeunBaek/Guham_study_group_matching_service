from django.shortcuts import render, redirect
from .forms import MatchPostForm
from .models import MatchPost
from django.contrib.auth.decorators import login_required

@login_required
def set_conditions(request):
    # 사용자가 정보를 입력하면 match:start 로 감
    if request.method == 'POST':
        form = MatchPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            context = {
                'form': form,
                'match_id': form.id,
            }
            return render(request, 'match/start.html', context)
            # return redirect("match:start", context )
        else:
            pass
    else:
        form = MatchPostForm()
    context = {
        'form': form
    }
    return render(request, 'match/set_conditions.html', context)


def start(request, match_id):
    form = MatchPost.objects.get(id=match_id)
    context = {
        'form':form,
        'match_id':match_id,
    }
    return render(request, 'match/start.html', context)

def success(request, user_id, match_id):
    form = MatchPost.objects.get(id=match_id)
    context = {
        'form': form,
        'match_id': form.id,
    }
    return render(request, 'match/success.html', context)

def accept(request):

    # 승낙 시 그룹 채팅방으로 이동
    pass



