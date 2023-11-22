class BookAlreadyExists(Exception):
    """Книга уже существует."""


class NoBooksAvailable(Exception):
    """Нет книг в базе."""


class AuthorAlreadyExists(Exception):
    """Автор уже существует."""


class AuthorNotFound(Exception):
    """Автор не найден."""


class NoAuthorsAvailable(Exception):
    """Ни одного автора не найдено."""


class UserAlreadyExists(Exception):
    """Пользователь уже существует."""


class BookNotFound(Exception):
    """Книга не найдена."""
