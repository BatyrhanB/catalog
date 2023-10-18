from rest_framework import generics, response, permissions

from user.services.favorite_services import FavoriteService
from user.serializers.favorite_serializers import FavoriteCreateSerializer
from user.models import Favorite


class FavoriteCreateAPIView(generics.CreateAPIView):
    """
    API for creating favorite
    """

    queryset = Favorite.objects.filter(is_deleted=False)
    serializer_class = FavoriteCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        FavoriteService.create_user_favorite(user=request.user, book_id=serializer.validated_data.get("book_id"))
        return response.Response({"message": "Favorite created successfully"})
