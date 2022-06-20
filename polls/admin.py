from django.contrib import admin
from .models import Author, Publisher, Book, Store


class BookInline(admin.TabularInline):
    model = Book
    extra = 2
    raw_id_fields = ['authors']


class AuthorsInLine(admin.TabularInline):
    model = Book.authors.through


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    date_hierarchy = 'book__pubdate'
    list_filter = ['book__authors']
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name']
    inlines = [AuthorsInLine, ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page', 'price', 'rating', 'publisher', 'pubdate']
    date_hierarchy = 'pubdate'
    filter_horizontal = ['authors']
    raw_id_fields = ['publisher']
    search_fields = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    date_hierarchy = 'book__pubdate'
    filter_horizontal = ['book']
    search_fields = ['name']
