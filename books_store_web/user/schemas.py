from ninja import Schema


class CustomUser(Schema):
    """Схема для создания пользователя."""

    username: str
    email: str
