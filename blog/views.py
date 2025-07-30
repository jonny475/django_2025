from django.shortcuts import render
from .models import Post

# 함수생성
def index(request):
    #db에서 query - select * from post
    posts = Post.objects.all()
    return render(request, 'blog/index.html',
                  context={'posts': posts}
                  )
def detail(request, pk):
    post111 = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html',
                  context={'post2': post111}
                  )
