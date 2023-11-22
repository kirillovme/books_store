import json
from http import HTTPStatus

from django.test import Client, TestCase
from user.factories import CustomUserFactory

BASE_URL = '/api/v1'


class CustomUserEndpointTest(TestCase):
    """Класс тестов для CustomUser enpoints."""

    def setUp(self):
        """Подготовка необходимых переменных."""
        self.client = Client()
        self.author = CustomUserFactory()
        self.user_data = {'username': 'someusername', 'email': 'someemail@gmail.com'}

    def test_create_user(self):
        """Тестирование создания пользователя."""
        response = self.client.post(BASE_URL + '/users', self.user_data, content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(json.loads(response.content)['username'], self.user_data['username'])
