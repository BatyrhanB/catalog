from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import BaseModel

from user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    # personal info
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Password")
    firstname = models.CharField(max_length=150, blank=True, null=True, verbose_name="First name")
    lastname = models.CharField(max_length=150, blank=True, null=True, verbose_name="Last name")
    middlename = models.CharField(max_length=150, blank=True, null=True, verbose_name="Middle name")

    # permissions
    is_superuser = models.BooleanField(default=False, verbose_name="SuperAdmin")
    is_admin = models.BooleanField(default=False, verbose_name="Admin")
    is_staff = models.BooleanField(default=False, verbose_name="Manager")
    is_verified = models.BooleanField(default=False, verbose_name="Verified")
    is_active = models.BooleanField(default=False, verbose_name="Active")

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-created_at",)


class Favorite(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="favorites", verbose_name="User")
    book = models.ForeignKey("catalog.Book", on_delete=models.CASCADE, related_name="favorites", verbose_name="Book")

    def __str__(self):
        return f"{self.user} - {self.book}"

    class Meta:
        db_table = "users__favorites"
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        ordering = ("-created_at",)
