from http import HTTPStatus
from typing import Any

from django.http import HttpRequest
from infrastructure.exceptions import UserAlreadyExists
from infrastructure.schemas import ResponseSchema
from ninja import Router
from user.schemas import CustomUser
from user.services import CustomUserService

user_router = Router(tags=['Users'])

user_service = CustomUserService()


@user_router.post(
    '',
    response={
        HTTPStatus.CREATED: CustomUser,
        HTTPStatus.BAD_REQUEST: ResponseSchema
    },
    description='Create user and send welcome email',
    summary='Create user'
)
def create_user(request: HttpRequest, payload: CustomUser) -> tuple[HTTPStatus, Any]:
    """Создание нового пользователя."""
    try:
        return HTTPStatus.CREATED, user_service.create_user(payload)
    except UserAlreadyExists:
        return HTTPStatus.BAD_REQUEST, {'message': 'This user already exists.'}
