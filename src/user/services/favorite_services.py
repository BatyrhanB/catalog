from user.models import Favorite
from catalog.models import Book


class FavoriteService(object):
    __favorite_model = Favorite
    __book_model = Book

    @classmethod
    def create_user_favorite(cls, user, book_id):
        """
        Create user favorite
        :param user: User instance
        :param book: Book instance
        :return: Favorite instance
        """
        book = cls.__book_model.objects.get(id=book_id)
        return cls.__favorite_model.objects.create(user=user, book=book)
