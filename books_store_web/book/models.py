from django.db import models


class Author(models.Model):
    """Модель автора книги."""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def str(self):
        return self.name


class Book(models.Model):
    """Модель книги."""

    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author)
    year_of_publish = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def str(self):
        return self.title
