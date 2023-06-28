from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('<int:pk>/', views.post_detail, name='post_detail'),  # 상세 페이지 URL 패턴 추가
    path('increase-views/<int:pk>/', views.increase_views, name='increase_views'),  # 조회수 증가 URL
]
