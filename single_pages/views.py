from django.shortcuts import render

# Create your views here.

# 함수 생성 

def landing(request):
    return render(request,
                  template_name='single_pages/landing.html',
                  context={'title':'Landing',
                           'name':'홍길동'}
                  )