from rest_framework import generics, permissions, response

from catalog.models import Review
from user.serializers.review_serializers import ReviewCreateSerializer
from user.services.review_services import ReviewService


class ReviewCreateAPIView(generics.CreateAPIView):
    """
    API for listing reviews
    :queryset: not deleted reviews
    """

    queryset = Review.objects.filter(is_deleted=False)
    serializer_class = ReviewCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ReviewService.create_user_review(
            user=request.user,
            book_id=serializer.validated_data.get("book_id"),
            rating=serializer.validated_data.get("rating"),
            review=serializer.validated_data.get("review"),
        )
        return response.Response({"message": "Favorite created successfully"})
