from django.shortcuts import render, redirect


def set_conditions(request):
    # 사용자가 정보를 입력하면 match:start 로 감
    if request.method == 'POST':
        context = {

        }
        redirect('match:start', context)
        pass
    else:
        context = {

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



