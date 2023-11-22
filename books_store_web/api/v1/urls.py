from book.api import author_router, book_router
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI(title='Book store API', description='API for book store')

api.add_router('/authors', author_router)
api.add_router('/books', book_router)

urlpatterns = [
    path('', api.urls)
]
