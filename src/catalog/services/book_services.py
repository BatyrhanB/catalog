from typing import Type

from django.db import models

from catalog.models import Book


class BookServices(object):
    """
    Class for working with books
    """

    __book_model = Book

    @classmethod
    def get_all_books(cls) -> Type[Book]:
        """
        Get not deleted books
        :return: QuerySet
        """
        return cls.__book_model.objects.filter(is_deleted=False).order_by("-created_at")

    @classmethod
    def get_average_rating(cls, book_instance: Type[Book]) -> float:
        """
        Get average rating for book
        :param book_instance: Book instance
        :return: float
        """
        return book_instance.reviews.aggregate(average_rating=models.Avg("rating"))["average_rating"] or 0.0
