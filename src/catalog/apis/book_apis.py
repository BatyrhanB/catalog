from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from catalog.services.book_services import BookServices
from catalog.serializers.book_serializers import BookListSerializer, BookDetailSerializer
from catalog.filters import BookDateRangeFilter


class BookListAPIView(generics.ListAPIView):
    """
    API for listing books
    :queryset: not deleted books
    :filters: genres, authors, created_at__gte, created_at__lte
    """
    queryset = BookServices.get_all_books()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookDateRangeFilter
    ordering_fields = ["created_at"]


class BookDetailAPIView(generics.RetrieveAPIView):
    """
    API for getting book by slug
    :queryset: not deleted books
    """
    queryset = BookServices.get_all_books()
    serializer_class = BookDetailSerializer
    lookup_field = "slug"
