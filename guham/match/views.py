from django.shortcuts import render, redirect
from .forms import MatchPostForm
from .models import MatchPost


# TODO 슬기 190618 set_conditions 수정
def set_conditions(request):
    # 사용자가 정보를 입력하면 match:start 로 감
    if request.method == 'POST':
        form = MatchPostForm(request.POST)
        if form.is_valid():
            context = {
                'form': form
            }
            return redirect('match:start', context)
        else:
            pass
    else:
        form = MatchPostForm()
        context = {
            'form': form
        }
        return render(request, 'match/set_conditions.html', context)


def start(request):
    context = {

    }
    return render(request, 'match/start.html', context)


def success(request):
    context = {

    }
    return render(request, 'match/success.html', context)


def accept(request):

    # 승낙 시 그룹 채팅방으로 이동
    pass



