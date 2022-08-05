from django.contrib import admin
from .models import Author, Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'born', 'country', 'description']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author']
