from django_filters import FilterSet, DateFilter

from catalog.models import Book


class BookDateRangeFilter(FilterSet):
    """
    Filter for books by date range
    :query_param_keys: created_at__gte, created_at__lte
    :example: /api/v1/books/list/?created_at__gte=2021-01-01&created_at__lte=2021-01-31
    """
    created_at__gte = DateFilter(field_name="created_at", lookup_expr="gte")
    created_at__lte = DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Book
        fields = ["genres", "authors"]
