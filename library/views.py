from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html',
                        context={'books': books}
                    )
def detail(request, pk):
    books1111 = Book.objects.get(pk=pk)
    return render(request, 'library/detail.html',
                  context={'book2': books1111}
                  )
