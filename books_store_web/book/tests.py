import json
from http import HTTPStatus

from book.factories import AuthorFactory, BookFactory
from django.test import Client, TestCase

BASE_URL = '/api/v1'


class AuthorEndpointTest(TestCase):
    """Класс тестов для Author enpoints."""

    def setUp(self):
        """Подготовка необходимых переменных."""
        self.client = Client()
        self.author = AuthorFactory()
        self.author_data = {'name': 'New Author', 'description': 'New author description'}
        self.updated_author_data = {'name': 'Updated Author', 'description': 'Updated description'}

    def test_get_authors(self):
        """Тестирование получения списка авторов."""
        response = self.client.get(BASE_URL + '/authors')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(json.loads(response.content)) >= 1)

    def test_create_author(self):
        """Тестирование создания автора."""
        response = self.client.post(BASE_URL + '/authors', self.author_data, content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(json.loads(response.content)['name'], self.author_data['name'])

    def test_get_author(self):
        """Тестирование получения автора по id."""
        response = self.client.get(BASE_URL + f'/authors/{self.author.id}')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.content)['id'], self.author.id)

    def test_update_author(self):
        """Тестирование обновления поле автора с определенным id."""
        response = self.client.patch(BASE_URL + f'/authors/{self.author.id}',
                                     data=json.dumps(self.updated_author_data),
                                     content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.content)['name'], self.updated_author_data['name'])

    def test_delete_author(self):
        """Тестирование удаления автора с определенным id."""
        response = self.client.delete(BASE_URL + f'/authors/{self.author.id}')
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        response = self.client.get(BASE_URL + f'/authors/{self.author.id}')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)


class BookEndpointTest(TestCase):
    """Класс тестов Book enpoints."""

    def setUp(self):
        """Подготовка необходимых переменных."""
        self.client = Client()
        self.author = AuthorFactory()
        self.book = BookFactory()
        self.book_data = {'title': 'New Book', 'year_of_publish': 2023, 'isbn': '1234567890123',
                          'authors': [self.author.id]}
        self.updated_book_data = {'title': 'Updated Book', 'year_of_publish': 2024,
                                  'isbn': '9876543210987', 'authors': [self.author.id]}

    def test_get_books(self):
        """Тестирование получения списка всех книг."""
        response = self.client.get(BASE_URL + '/books')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(len(json.loads(response.content)) >= 1)

    def test_create_book(self):
        """Тестирование создания книги."""
        response = self.client.post(BASE_URL + '/books', self.book_data, content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(json.loads(response.content)['title'], self.book_data['title'])

    def test_get_book(self):
        """Тестирование получения книги с определенным id."""
        response = self.client.get(BASE_URL + f'/books/{self.book.id}')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.content)['id'], self.book.id)

    def test_update_book(self):
        """Тестирование обновления книги с определенным id."""
        response = self.client.patch(BASE_URL + f'/books/{self.book.id}',
                                     data=json.dumps(self.updated_book_data),
                                     content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(response.content)['title'], self.updated_book_data['title'])

    def test_delete_book(self):
        """Тестирование удаления книги с определенным id."""
        response = self.client.delete(BASE_URL + f'/books/{self.book.id}')
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        response = self.client.get(BASE_URL + f'/books/{self.book.id}')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
