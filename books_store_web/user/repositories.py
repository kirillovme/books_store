from user.models import CustomUser as CustomUserModel
from user.schemas import CustomUser as CustomUserScheme


class CustomUserRepository:
    """Репозиторий для работы с моделью CustomUser."""

    @staticmethod
    def create_user(user_data: CustomUserScheme) -> CustomUserModel:
        """Создание пользователя."""
        return CustomUserModel.objects.create(**user_data.dict())
