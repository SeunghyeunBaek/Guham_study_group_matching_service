from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),  # 전체 글 보기
    path('<int:post_id>/detail/', views.detail, name='detail'),  # 스터디 모집 글 열람

    path('create/', views.create, name='create'),  # 스터디 모집 글 생성
    path('<int:post_id>/delete/', views.delete, name='delete'),  # 스터디 모집 글 삭제
    path('<int:post_id>/update/', views.update, name='update'),  # 스터디 모집 글 수정

    path('search/', views.search, name='search'),  # 스터디 모집글 필터 검색
    path('<int:post_id>/apply/', views.apply, name='apply'), # 스터디 지원

    path('test/', views.test, name='test'),
]
