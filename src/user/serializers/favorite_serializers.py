from rest_framework import serializers


class FavoriteCreateSerializer(serializers.Serializer):
    """
    Serializer for creating favorite
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book_id = serializers.UUIDField(required=True)
