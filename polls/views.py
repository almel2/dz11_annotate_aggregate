from django.shortcuts import render, get_object_or_404
from .models import Book, Author


def index(request):
    return render(request, 'polls/index.html')


def book_list(request):
    books = Book.objects.all()[:100]
    context = {
        'books': books,
    }
    return render(request, 'polls/book_list.html', context)


def book_detaile(request, pk_book):
    book = get_object_or_404(Book, pk=pk_book)
    context = {
        'book': book,
    }
    return render(request, 'polls/book_detaile.html', context)


def author_list(request):
    authors = Author.objects.all()[:100]
    context = {
        'authors': authors,
    }
    return render(request, 'polls/author_list.html', context)


def authors_detaile(request, pk_author):
    author = get_object_or_404(Author, pk=pk_author)
    context = {
        'author': author
    }
    return render(request, 'polls/author_detaile.html', context)