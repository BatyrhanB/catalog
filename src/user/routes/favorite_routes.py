from django.urls import path

from user.apis.favorite_apis import FavoriteCreateAPIView

urlpatterns = [
    path("create/", FavoriteCreateAPIView.as_view(), name="favorite-create"),
]
