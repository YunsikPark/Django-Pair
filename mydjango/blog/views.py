from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    # post_obj = Post.objects.all()
    title = "블리자드 오버워치 영웅 프로필"
    context = {
        'post_list':Post.objects.all().order_by('-create_time'),
        'title':  title
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context={
        'title': post.title,
        'text' : post.text
    }

    return render(request, 'blog/post_detail.html', context)

def post_add(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_add.html', context)
    elif request.method == 'POST':
        user = get_user_model()
        title = request.POST['title']
        text = request.POST['text']
        pt = Post.objects.create(
            title=title,
            text=text,
            author = user.objects.first()
        )
        return redirect('post_detail', pk=pt.pk)
