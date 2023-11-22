from ninja import Schema


class AuthorCreate(Schema):
    """Схема для создания автора."""

    name: str
    description: str


class AuthorOut(Schema):
    """Схема для вывода информации об авторе."""

    id: int
    name: str
    description: str


class AuthorUpdate(Schema):
    """Схема для обновления информации об авторе."""

    name: str | None
    description: str | None


class BookCreate(Schema):
    """Схема для создания книги."""

    title: str
    year_of_publish: int
    isbn: str
    authors: list[int]


class BookOut(Schema):
    """Схема для вывода информации о книге."""

    id: int
    title: str
    year_of_publish: int
    isbn: str
    authors: list[AuthorOut]


class BookUpdate(Schema):
    """Схема для обновления информации о книге."""

    title: str | None
    year_of_publish: int | None
    isbn: str | None
    authors: list[int] | None
