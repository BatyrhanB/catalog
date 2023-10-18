from rest_framework import serializers

from catalog.models import Author


class AuthorInnerSerializer(serializers.ModelSerializer):
    """
    Author serializer for BookListSerializer
    """
    class Meta:
        model = Author
        fields = ["full_name"]
