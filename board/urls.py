from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
]
