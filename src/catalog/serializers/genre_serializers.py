from rest_framework import serializers

from catalog.models import Genre


class GenreInnerSerializer(serializers.ModelSerializer):
    """
    Genre serializer for BookListSerializer
    """
    class Meta:
        model = Genre
        fields = ["name"]
