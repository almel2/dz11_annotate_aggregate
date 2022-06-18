from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=150)


class Book(models.Model):
    name = models.CharField(max_length=150)
    page = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField('polls.Author')
    publisher = models.ForeignKey('polls.Publisher', on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=150)
    book = models.ManyToManyField('polls.Book')
