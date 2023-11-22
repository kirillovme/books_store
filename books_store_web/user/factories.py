from factory import Faker
from factory.django import DjangoModelFactory
from user.models import CustomUser


class CustomUserFactory(DjangoModelFactory):
    """Фабрика для создания тестовых пользователей."""

    class Meta:
        model = CustomUser

    username = Faker('user_name')
    email = Faker('email')
