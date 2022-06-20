from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, 'polls/index.html')


def book_list(request):
    books = Book.objects.all()[:100]
    context = {
        'books': books,
    }
    return render(request, 'polls/book_list.html', context)