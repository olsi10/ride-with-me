from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'board/post_list.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'board/post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.views = 0  # 조회수 초기화
            post.save()
            return redirect('board:post_list')
    else:
        form = PostForm()

    return render(request, 'board/post_create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # 폼 데이터를 받아 새로운 게시물 생성
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:post_list')
    else:
        form = PostForm()

    return render(request, 'board/post_detail.html', {'post': post, 'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('board:post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'board/post_edit.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('board:post_list')

def increase_views(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return redirect('board:post_detail', pk=post.pk)
