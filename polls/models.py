from django.db import models
from django.urls import reverse

class MyMeta:
    class Meta:
        ordering = ['id']

class Author(models.Model, MyMeta):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Publisher(models.Model, MyMeta):
    name = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('publisher_detaile', kwargs={'pk_publisher': self.pk})

    def __str__(self):
        return f'Publisher - {self.name}'


class Book(models.Model, MyMeta):
    name = models.CharField(max_length=150)
    page = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField('polls.Author')
    publisher = models.ForeignKey('polls.Publisher', on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return f'Book - {self.name}'


class Store(models.Model, MyMeta):
    name = models.CharField(max_length=150)
    book = models.ManyToManyField('polls.Book')

    def get_absolute_url(self):
        return reverse('store_detaile', kwargs={'pk_store': self.pk})

    def __str__(self):
        return f'Store - {self.name}'
