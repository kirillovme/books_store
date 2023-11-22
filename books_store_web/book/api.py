from http import HTTPStatus
from typing import Any

from book.schemas import (
    AuthorCreate,
    AuthorOut,
    AuthorUpdate,
    BookCreate,
    BookOut,
    BookUpdate,
)
from book.services import AuthorService, BookService
from django.http import HttpRequest
from infrastructure.exceptions import (
    AuthorAlreadyExists,
    AuthorNotFound,
    BookAlreadyExists,
    BookNotFound,
    NoAuthorsAvailable,
    NoBooksAvailable,
)
from infrastructure.schemas import ResponseSchema
from ninja import Router

author_router = Router(tags=['Authors'])
book_router = Router(tags=['Books'])

author_service = AuthorService()
book_service = BookService()


@author_router.get(
    '',
    response={
        HTTPStatus.OK: list[AuthorOut],
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Get all authors',
    summary='Get all authors'
)
def get_authors(request: HttpRequest) -> tuple[HTTPStatus, Any]:
    """Получение списка авторов."""
    try:
        return HTTPStatus.OK, author_service.get_authors()
    except NoAuthorsAvailable:
        return HTTPStatus.NOT_FOUND, {'message': 'No authors currently in database.'}


@author_router.post(
    '',
    response={
        HTTPStatus.CREATED: AuthorOut,
        HTTPStatus.BAD_REQUEST: ResponseSchema
    },
    description='Create author',
    summary='Create author'
)
def create_author(request: HttpRequest, payload: AuthorCreate) -> tuple[HTTPStatus, Any]:
    """Создание нового автора."""
    try:
        return HTTPStatus.CREATED, author_service.create_author(payload)
    except AuthorAlreadyExists:
        return HTTPStatus.BAD_REQUEST, {'message': 'Author already exists.'}


@author_router.get(
    '{author_id}',
    response={
        HTTPStatus.OK: AuthorOut,
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Get author by id',
    summary='Get author'
)
def get_author(request: HttpRequest, author_id: int) -> tuple[HTTPStatus, Any]:
    """Получение автора по id."""
    try:
        return HTTPStatus.OK, author_service.get_author(author_id)
    except AuthorNotFound:
        return HTTPStatus.NOT_FOUND, {'message': f'Author with id:{author_id} not found.'}


@author_router.patch(
    '{author_id}',
    response={
        HTTPStatus.OK: AuthorOut,
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Update author by id',
    summary='Update author'
)
def update_author(request: HttpRequest, author_id: int, payload: AuthorUpdate) -> tuple[HTTPStatus, Any]:
    """Обновление автора с указанным id."""
    try:
        return HTTPStatus.OK, author_service.update_author(author_id, payload)
    except AuthorNotFound:
        return HTTPStatus.NOT_FOUND, {'message': f'Author with id:{author_id} not found.'}


@author_router.delete(
    '{author_id}',
    response={
        HTTPStatus.NO_CONTENT: None,
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Delete author by id',
    summary='Delete author'
)
def delete_author(request: HttpRequest, author_id: int) -> tuple[HTTPStatus, dict[str, Any]]:
    """Удаление автора с указанным id."""
    try:
        author_service.delete_author(author_id)
        return HTTPStatus.NO_CONTENT, {}
    except AuthorNotFound:
        return HTTPStatus.NOT_FOUND, {'message': f'Author with id:{author_id} not found.'}


@book_router.get(
    '',
    response={
        HTTPStatus.OK: list[BookOut],
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Get all books',
    summary='Get all books'
)
def get_books(request: HttpRequest) -> tuple[HTTPStatus, Any]:
    """Получение списка книг."""
    try:
        return HTTPStatus.OK, book_service.get_books()
    except NoBooksAvailable:
        return HTTPStatus.NOT_FOUND, {'message': 'No books currently in database.'}


@book_router.post(
    '',
    response={
        HTTPStatus.CREATED: BookOut,
        HTTPStatus.BAD_REQUEST: ResponseSchema
    },
    description='Create book',
    summary='Create book'
)
def create_book(request: HttpRequest, payload: BookCreate) -> tuple[HTTPStatus, Any]:
    """Создание новой книги."""
    try:
        return HTTPStatus.CREATED, book_service.create_book(payload)
    except BookAlreadyExists:
        return HTTPStatus.BAD_REQUEST, {'message': 'Book already exists.'}


@book_router.get(
    '{book_id}',
    response={
        HTTPStatus.OK: BookOut,
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Get book by id',
    summary='Get book'
)
def get_book(request: HttpRequest, book_id: int) -> tuple[HTTPStatus, Any]:
    """Получение книги по id."""
    try:
        return HTTPStatus.OK, book_service.get_book(book_id)
    except BookNotFound:
        return HTTPStatus.NOT_FOUND, {'message': f'Book with id:{book_id} not found.'}


@book_router.patch(
    '{book_id}',
    response={
        HTTPStatus.OK: BookOut,
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Update book by id',
    summary='Update book'
)
def update_book(request: HttpRequest, book_id: int, payload: BookUpdate) -> tuple[HTTPStatus, Any]:
    """Обновление книги с указанным id."""
    try:
        return HTTPStatus.OK, book_service.update_book(book_id, payload)
    except BookNotFound:
        return HTTPStatus.NOT_FOUND, {'message': f'Book with id:{book_id} not found.'}


@book_router.delete(
    '{book_id}',
    response={
        HTTPStatus.NO_CONTENT: None,
        HTTPStatus.NOT_FOUND: ResponseSchema
    },
    description='Delete book by id',
    summary='Delete book'
)
def delete_book(request: HttpRequest, book_id: int) -> tuple[HTTPStatus, dict[str, Any]]:
    """Удаление книги с указанным id."""
    try:
        book_service.delete_book(book_id)
        return HTTPStatus.NO_CONTENT, {}
    except BookNotFound:
        return HTTPStatus.NOT_FOUND, {'message': f'Book with id:{book_id} not found.'}
