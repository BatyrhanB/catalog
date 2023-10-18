from django.urls import path, include


urlpatterns = [
    path("book/", include("catalog.routes.book_routes"), name="book-main"),
]
