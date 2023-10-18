from typing import Type

from user.models import User
from catalog.models import Review, Book


class ReviewService(object):
    """
    Service for user review to book
    """

    __review_model = Review
    __book_model = Book

    @classmethod
    def create_user_review(cls, book_id: str, user: Type[User], review: str, rating: int) -> None:
        """
        Review creation by user
        :args
            book_id: UUID
            user: User instance
            review: str
            rating: int
        :return: None
        """
        book = cls.__book_model.objects.get(id=book_id)

        return cls.__review_model.objects.create(user=user, book=book, review=review, rating=rating)
