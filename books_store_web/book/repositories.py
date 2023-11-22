from book.models import Author, Book
from book.schemas import AuthorCreate, AuthorUpdate, BookCreate, BookUpdate


class AuthorRepository:
    """Репозиторий для работы с моделью Author."""

    @staticmethod
    def get_authors() -> list[Author]:
        """Получает список всех авторов."""
        return Author.objects.all()

    @staticmethod
    def create_author(author_data: AuthorCreate) -> Author:
        """Создание автора."""
        return Author.objects.create(**author_data.dict())

    @staticmethod
    def get_author(author_id: int) -> Author:
        """Получение автора по id."""
        return Author.objects.get(id=author_id)

    @staticmethod
    def delete_author(author_id: int) -> None:
        """Удаляет автора по id."""
        Author.objects.get(id=author_id).delete()

    @staticmethod
    def update_author(author_id: int, author_data: AuthorUpdate) -> Author:
        """Обновляет часть полей автора с указанным id."""
        author = Author.objects.get(id=author_id)
        author_data_dict = author_data.dict(exclude_none=True)
        for key, value in author_data_dict.items():
            setattr(author, key, value)
        author.save()
        return author


class BookRepository:
    @staticmethod
    def get_books() -> list[Book]:
        """Получает список всех книг."""
        return Book.objects.all()

    @staticmethod
    def create_book(book_data: BookCreate) -> Book:
        """Создание книги."""
        book = Book.objects.create(**book_data.dict(exclude={'authors'}))
        book.authors.set(book_data.authors)
        return book

    @staticmethod
    def get_book(book_id: int) -> Book:
        """Получение книги по id."""
        return Book.objects.get(id=book_id)

    @staticmethod
    def delete_book(book_id: int) -> None:
        """Удаляет книгу по id."""
        return Book.objects.get(id=book_id).delete()

    @staticmethod
    def update_book(book_id: int, book_data: BookUpdate) -> Book:
        """Обновляет часть полей книги с указанным id."""
        book = Book.objects.get(id=book_id)
        book_data_dict = book_data.dict(exclude_none=True)
        authors = book_data_dict.pop('authors', None)
        for key, value in book_data_dict.items():
            setattr(book, key, value)
        if authors is not None:
            book.authors.set(authors)
        book.save()
        return book
