from django.urls import path
from . import views

app_name = 'match'

urlpatterns = [
    path('', views.set_conditions, name='set_conditions'),  # 매칭 전 조건 설정
    # path('<int:match_id>/', views.detail, name='detail'),  # 조건 확인, 매칭 준비
    # path('<int:match_id>/start/', views.start, name='start'),  # 매칭 시작
    # TODO path('success/<int:match_id>/', views.success, name='success'),  # 매칭 완료
    # TODO path('accept/', views.accept, name='accept'),  # 매칭 승낙
]
