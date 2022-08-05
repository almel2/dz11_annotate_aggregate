from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    born = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.CharField(max_length=1000)
    author = models.ForeignKey('celery_app.Author', on_delete=models.CASCADE)

    def __str__(self):
        return f'Quote'

