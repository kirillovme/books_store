from django.db import IntegrityError
from infrastructure.exceptions import UserAlreadyExists
from user.models import CustomUser as CustomUserModel
from user.repositories import CustomUserRepository
from user.schemas import CustomUser as CustomUserScheme
from user.tasks import send_welcome_email


class CustomUserService:
    """Сервисный слой для модели User."""

    def __init__(self):
        self.repo = CustomUserRepository

    def create_user(self, user_data: CustomUserScheme) -> CustomUserModel:
        """Создание пользователя и отправка письма."""
        try:
            user = self.repo.create_user(user_data)
            send_welcome_email.delay(user_data.email)
            return user
        except IntegrityError:
            raise UserAlreadyExists
