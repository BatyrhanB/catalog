from rest_framework import serializers

from catalog.models import Review


class ReviewInnerSerializer(serializers.ModelSerializer):
    """
    Review serializer for BookDetailSerializer
    """
    class Meta:
        model = Review
        fields = ["review", "rating",]
