from rest_framework import serializers


class ReviewCreateSerializer(serializers.Serializer):
    """
    Serializer for creating review
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book_id = serializers.UUIDField(required=True)
    review = serializers.CharField(required=True)
    rating = serializers.IntegerField(required=True)
