from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # 회원가입
    path('login/', views.login, name='login'),  # 로그인
    path('logout/', views.logout, name='logout'),  # 로그아웃
    path('<int:user_id>/update/', views.update, name='update'),  # 회원정보 수정

    path('<int:user_id>/', views.user_page, name='user_page'),  # 유저 페이지
    path('<int:user_id>/pick/', views.pick, name='pick'),  # 장바구니에 담기
    path('<int:user_id>/pick/clean/', views.clean, name='clean')  # 픽 지우기
]
