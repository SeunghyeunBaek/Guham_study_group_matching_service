from django.urls import path
from . import views

app_name = 'match'

urlpatterns = [
    path('', views.set_conditions, name='set_conditions'),  # 매칭 전 조건 설정
    path('start/', views.start, name='start'),  # 매칭 시작
    path('success/', views.success, name='success'),  # 매칭 완료
    path('accept/', views.accept, name='accept'),  # 매칭 승낙
]