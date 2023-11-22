from book.models import Author, Book
from book.repositories import AuthorRepository, BookRepository
from book.schemas import AuthorCreate, AuthorUpdate, BookCreate, BookUpdate
from django.db import IntegrityError
from infrastructure.exceptions import (
    AuthorAlreadyExists,
    AuthorNotFound,
    BookAlreadyExists,
    BookNotFound,
    NoAuthorsAvailable,
    NoBooksAvailable,
)


class AuthorService:
    """Сервисный слой для модели Author."""

    def __init__(self):
        self.repo = AuthorRepository

    def get_authors(self) -> list[Author]:
        """Получение списка авторов и обработка ошибок."""
        if authors := self.repo.get_authors():
            return authors
        else:
            raise NoAuthorsAvailable

    def create_author(self, author_data: AuthorCreate) -> Author:
        """Создание автора и обработка ошибок."""
        try:
            return self.repo.create_author(author_data)
        except IntegrityError:
            raise AuthorAlreadyExists

    def get_author(self, author_id: int) -> Author:
        """Получение автора по id и обработка ошибок."""
        try:
            return self.repo.get_author(author_id)
        except Author.DoesNotExist:
            raise AuthorNotFound

    def update_author(self, author_id: int, author_data: AuthorUpdate) -> Author:
        """Обновление автора с указанным id и обработка ошибок."""
        try:
            return self.repo.update_author(author_id, author_data)
        except Author.DoesNotExist:
            raise AuthorNotFound

    def delete_author(self, author_id: int) -> None:
        """Удаление автора с указанным id и обработка ошибок."""
        try:
            self.repo.delete_author(author_id)
        except Author.DoesNotExist:
            raise AuthorNotFound


class BookService:
    """Сервисный слой для модели Book."""

    def __init__(self):
        self.repo = BookRepository

    def get_books(self) -> list[Book]:
        """Получение списка книг и обработка ошибок."""
        if books := self.repo.get_books():
            return books
        else:
            raise NoBooksAvailable

    def create_book(self, book_data: BookCreate) -> Book:
        """Создание книги и обработка ошибок."""
        try:
            return self.repo.create_book(book_data)
        except IntegrityError:
            raise BookAlreadyExists

    def get_book(self, book_id: int) -> Book:
        """Получение книги по id и обработка ошибок."""
        try:
            return self.repo.get_book(book_id)
        except Book.DoesNotExist:
            raise BookNotFound

    def update_book(self, book_id: int, book_data: BookUpdate) -> Book:
        """Обновление книги с указанным id и обработка ошибок."""
        try:
            return self.repo.update_book(book_id, book_data)
        except Book.DoesNotExist:
            raise BookNotFound

    def delete_book(self, book_id: int) -> None:
        """Удаление книги с указанным id и обработка ошибок."""
        try:
            self.repo.delete_book(book_id)
        except Book.DoesNotExist:
            raise BookNotFound
