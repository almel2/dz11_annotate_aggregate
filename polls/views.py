from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Store, Publisher
from django.db.models import Avg, Max, Count


def index(request):
    books = Book.objects.all()
    agg = books.aggregate(Max('rating'), Max('price'), Avg('price'), Count('id'))
    ann = books.annotate(Count('authors'))
    context = {
        'agg': agg,
        'ann': ann,
    }
    return render(request, 'polls/index.html', context)


def book_list(request):
    books = Book.objects.select_related('publisher').prefetch_related('authors').all()
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
    #  authors = Author.objects.all()
    authors = Author.objects.prefetch_related('book_set').all()
    context = {
        'authors': authors,
    }
    return render(request, 'polls/author_list.html', context)


def authors_detaile(request, pk_author):
    author = get_object_or_404(Author, pk=pk_author)
    context = {
        'author': author,
    }
    return render(request, 'polls/author_detaile.html', context)


def store_list(request):
    #  storeis = Store.objects.all().iterator()
    storeis = Store.objects.prefetch_related('book').all()
    contxt = {
        'storeis': storeis,
    }
    return render(request, 'polls/store_list.html', contxt)


def store_detaile(request, pk_store):
    store = get_object_or_404(Store, pk=pk_store)
    context = {
        'store': store,
    }
    return render(request, 'polls/store_detaile.html', context)


def publisher_list(request):
    #  publishers = Publisher.objects.all()[:100]
    publishers = Publisher.objects.prefetch_related('book_set')
    context = {
        'publishers': publishers,
    }
    return render(request, 'polls/publisher_list.html', context)


def publisher_detaile(request, pk_publisher):
    pubkisher = get_object_or_404(Publisher, pk=pk_publisher)
    context = {
        'publisher': pubkisher,
    }
    return render(request, 'polls/publisher_detaile.html', context)
