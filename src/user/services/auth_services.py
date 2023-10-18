from typing import Union
from django.db import transaction

from common.exceptions import UserAlreadyExistException, SomethingGetWrongException
from common.validators.password_validators import validate_user_password
from user.models import User


class AuthService(object):
    __user_model = User

    @classmethod
    def signup(cls, email: str, password: str, confirm_password: str, **kwargs) -> Union[dict, None]:
        """
        User sign up
        :args
            email (str): _user's email_
            password (str): _user's password_
            confirm_password (str): _confirm password_
        :raises
            AlreadyExist: _return statusCode about already existing user_
            SomethingGetWrongException: _return statusCode about unknown server error_
        :returns
            Union[dict, None]: _return message about user succesfully signed up,
            and need to verify it or None what means exceptions object_
        """
        exist_user: User = cls.__user_model.objects.filter(email=email).first()
        if exist_user and exist_user.is_active and exist_user.is_verified:
            raise UserAlreadyExistException({"message": "User already exist"})

        verified_password: str = validate_user_password(password, confirm_password)
        try:
            with transaction.atomic():
                if exist_user:
                    exist_user.set_password(verified_password)
                    exist_user.save()
                else:
                    cls.__user_model.objects.create_user(email=email, password=verified_password, **kwargs)
                response: dict = {"message": "User successfully signed up, please verify your email"}
                return response
        except Exception:
            raise SomethingGetWrongException({"message": "Something get wrong"})
