from django.urls import path

from user.apis.auth_apis import SignUpAPIView


urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="user-sign-up"),
]
