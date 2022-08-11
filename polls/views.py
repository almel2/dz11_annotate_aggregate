from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import AddStoreForm, PublisherAddForm
from .models import Book, Author, Store, Publisher
from django.db.models import Avg, Max, Count
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class Index(ListView):
    model = Book
    template_name = 'polls/index.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agg'] = Book.objects.all().aggregate(Max('rating'), Max('price'), Avg('price'), Count('id'))
        context['ann'] = Book.objects.all().annotate(Count('publisher'))
        return context


# def index(request):
#     books = Book.objects.all()
#     agg = books.aggregate(Max('rating'), Max('price'), Avg('price'), Count('id'))
#     ann = books.annotate(Count('publisher'))
#     context = {
#         'agg': agg,
#         'ann': ann,
#     }
#     return render(request, 'polls/index.html', context)


class BookList(ListView):
    model = Book
    template_name = 'polls/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.select_related('publisher').prefetch_related('authors').all()
        return context


#  def book_list(request):
#      books = Book.objects.select_related('publisher').prefetch_related('authors').all()
#      context = {
#          'books': books,
#      }
#      return render(request, 'polls/book_list.html', context)


class BookDetaile(DetailView):
    model = Book
    template_name = 'polls/book_detaile.html'
    pk_url_kwarg = 'pk_book'


# def book_detaile(request, pk_book):
#     book = get_object_or_404(Book, pk=pk_book)
#     context = {
#         'book': book,
#     }
#     return render(request, 'polls/book_detaile.html', context)


class AuthorsList(ListView):
    model = Author
    template_name = 'polls/author_list.html'
    context_object_name = 'authors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.prefetch_related('book_set').all()
        return context


#  def author_list(request):
#      #  authors = Author.objects.all()
#      authors = Author.objects.prefetch_related('book_set').all()
#      context = {
#          'authors': authors,
#      }
#      return render(request, 'polls/author_list.html', context)


class AuthorDetaile(DetailView):
    model = Author
    template_name = 'polls/author_detaile.html'
    pk_url_kwarg = 'pk_author'


# def authors_detaile(request, pk_author):
#     author = get_object_or_404(Author, pk=pk_author)
#     context = {
#         'author': author,
#     }
#     return render(request, 'polls/author_detaile.html', context)


class StoreList(ListView):
    model = Store
    template_name = 'polls/store_list.html'
    context_object_name = 'storeis'
    paginate_by = 10

    #def get_context_data(self, *, object_list=None, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['storeis'] = Store.objects.prefetch_related('book').all()
    #    return context


# def store_list(request):
#     #  storeis = Store.objects.all().iterator()
#     storeis = Store.objects.prefetch_related('book').all()
#     contxt = {
#         'storeis': storeis,
#     }
#     return render(request, 'polls/store_list.html', contxt)


class StoreDetaile(DetailView):
    model = Store
    template_name = 'polls/store_detaile.html'
    pk_url_kwarg = 'pk_store'


# def store_detaile(request, pk_store):
#     store = get_object_or_404(Store, pk=pk_store)
#     context = {
#         'store': store,
#     }
#     return render(request, 'polls/store_detaile.html', context)


class StoreAdd(LoginRequiredMixin, CreateView):
    model = Store
    form_class = AddStoreForm
    template_name = 'polls/store_add_form.html'


class StoreUpdate(LoginRequiredMixin, UpdateView):
    model = Store
    form_class = AddStoreForm
    template_name = 'polls/store_add_form.html'
    pk_url_kwarg = 'pk_store'


class StoreDelete(LoginRequiredMixin, DeleteView):
    model = Store
    pk_url_kwarg = 'pk_store'
    template_name = 'polls/store_delete.html'
    success_url = reverse_lazy('store_list')


class PublisherList(ListView):
    model = Publisher
    template_name = 'polls/publisher_list.html'
    context_object_name = 'publishers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishers'] = Publisher.objects.prefetch_related('book_set')
        return context


# def publisher_list(request):
#     # publishers = Publisher.objects.all()[:100]
#     publishers = Publisher.objects.prefetch_related('book_set')
#     # publishers = Publisher.objects.select_related('book_set')
#     context = {
#         'publishers': publishers,
#     }
#     return render(request, 'polls/publisher_list.html', context)


class PublisherDetaile(DetailView):
    model = Publisher
    template_name = 'polls/publisher_detaile.html'
    pk_url_kwarg = 'pk_publisher'


# def publisher_detaile(request, pk_publisher):
#     pubkisher = get_object_or_404(Publisher, pk=pk_publisher)
#     context = {
#         'publisher': pubkisher,
#     }
#     return render(request, 'polls/publisher_detaile.html', context)


# @login_required(login_url='/accounts/login/')
# def store_add(request):
#     if request.method == 'POST':
#         form = AddStoreForm(request.POST)
#         if form.is_valid():
#             name_store = form.cleaned_data['name']
#             book_objects = form.cleaned_data['book']
#             try:
#                 store_obj = Store.objects.create(name=name_store)
#                 store_obj.book.add(*book_objects)
#
#                 return redirect('success')
#             except:
#                 form.add_error(None, 'Error create object')
#     else:
#         form = AddStoreForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'polls/store_add_form.html', context)


class PublisherAdd(LoginRequiredMixin, CreateView):
    model = Publisher
    form_class = PublisherAddForm
    template_name = 'polls/publisher_add_form.html'


class PublisherUpdate(LoginRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherAddForm
    template_name = 'polls/publisher_add_form.html'
    pk_url_kwarg = 'pk_publisher'

class PublisherDelete(LoginRequiredMixin, DeleteView):
    model = Publisher
    template_name = 'polls/publisher_delete.html'
    pk_url_kwarg = 'pk_publisher'
    success_url = reverse_lazy('publisher_list')


def success(request):
    return render(request, 'polls/success.html', {})