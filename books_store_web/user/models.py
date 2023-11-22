from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    """Модель кастомного пользователя."""
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(default=timezone.now)
