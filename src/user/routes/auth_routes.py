from django.urls import path

from user.apis.auth_apis import SignUpAPIView, UserVerificationAPIView


urlpatterns = [
    path("signup/", SignUpAPIView.as_view(), name="user-sign-up"),
    path("verify/", UserVerificationAPIView.as_view(), name="user-verify"),
]
