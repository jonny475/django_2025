import os
from fileinput import filename

from django.http import FileResponse
from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView

from .forms import PostForm
from .models import Post, Category
from django.conf import settings

#CBV
# #class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#
# class DetailPostView(DetailView):
#     model = Post
#     context_object_name = 'post'

# 함수생성
def index(request):
    #db에서 query - select * from post
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request, 'blog/index.html',
                  context={'posts': posts,
                            'categories':categories
                           }
                  )


def category(request, slug):
    categories = Category.objects.all()  # category list 다 줘
    if slug == 'no_category':            #미분류인경우
        posts = Post.objects.filter(category=None)
    else:                                # 카테고리가 있는 경우
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)

    return render(request, template_name='blog/index.html',
                       context={'posts': posts,
                                'categories':categories
                                 }
                      )

def detail(request, pk):
    post111 = Post.objects.get(pk=pk)
    categories = Category.objects.all().order_by('-pk')
    return render(request, 'blog/detail.html',
                  context={'post': post111,
                           'categories':categories
                           }
                  )

def create(request):
    categories = Category.objects.all().order_by('-pk')
    if request.method == "POST": #작성하다가 제출 버튼을 누른 경우
        postform = PostForm(request.POST,request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title = post1.title + "졸려"
            post1.save()     #정상값인 경우

            return redirect('/blog/')
    else:                        #get 내가 새글 작성하기 버튼을 눌러서 create 함수로 준비가 들어온것

        postform = PostForm()
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform': postform,
                           'categories': categories
                           }
                  )


def createfake(request):
    post = Post()
    post.title = "새싹 용산구"
    post.content = "나진상가 3층"
    post.save()
    return redirect('/blog/')

def upload(request):
    if request.method == "POST":
        postform =  PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
        return redirect('/blog/')
    else:
        postform = PostForm()

    return render(request,
                  template_name='blog/postform.html',
                  context={'postform': postform}
                  )


def download(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
            raise Http404("파일을 찾을 수 없습니다.")



