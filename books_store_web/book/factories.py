from factory import Faker
from factory.django import DjangoModelFactory

from book.models import Author, Book


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = Faker('name')
    description = Faker('text')


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = Faker('sentence')
    year_of_publish = Faker('year')
    isbn = Faker('isbn13', separator='')
