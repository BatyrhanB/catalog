from rest_framework import generics, response

from user.serializers.auth_serializers import SignUpSerializer
from user.services.auth_services import AuthService


class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    """
    API for signing up
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = AuthService.signup(
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
            confirm_password=serializer.validated_data.get("confirm_password"),
        )
        return response.Response(result)
