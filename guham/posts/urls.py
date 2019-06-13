from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='detail'),
    path('<int:post_id>/create/', views.create, name='create'),
]
