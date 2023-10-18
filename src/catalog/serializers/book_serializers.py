from rest_framework import serializers

from catalog.models import Book
from catalog.services.book_services import BookServices
from catalog.serializers import author_serializers, genre_serializers, review_serializers


class BookListSerializer(serializers.ModelSerializer):
    """
    Book serializer for List API View
    """

    genres = genre_serializers.GenreInnerSerializer(many=True)
    authors = author_serializers.AuthorInnerSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "name", "slug", "average_rating", "genres", "authors"]

    def get_average_rating(self, obj):
        return BookServices.get_average_rating(obj)


class BookDetailSerializer(BookListSerializer):
    """
    Book serializer for Detail API View
    """

    reviews = review_serializers.ReviewInnerSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            "name",
            "slug",
            "description",
            "average_rating",
            "genres",
            "authors",
            "reviews",
            "created_at",
            "updated_at",
        ]
