from django.urls import path

from user.apis.review_apis import ReviewCreateAPIView


urlpatterns = [
    path("create/", ReviewCreateAPIView.as_view(), name="review-create"),
]
