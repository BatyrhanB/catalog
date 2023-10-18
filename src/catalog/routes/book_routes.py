from django.urls import path

from catalog.apis.book_apis import BookListAPIView
from catalog.apis.book_apis import BookDetailAPIView


urlpatterns = [
    path("list/", BookListAPIView.as_view(), name="books-list"),
    path("<slug:slug>/", BookDetailAPIView.as_view(), name="book-detail"),
]
