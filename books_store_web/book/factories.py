from book.models import Author, Book
from factory import Faker
from factory.django import DjangoModelFactory


class AuthorFactory(DjangoModelFactory):
    """Фабрика для создания тестовых авторов."""

    class Meta:
        model = Author

    name = Faker('name')
    description = Faker('text')


class BookFactory(DjangoModelFactory):
    """Фабрика для создания тестовых книг."""

    class Meta:
        model = Book

    title = Faker('sentence')
    year_of_publish = Faker('year')
    isbn = Faker('isbn13', separator='')
