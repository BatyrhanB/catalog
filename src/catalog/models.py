from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False, verbose_name=_("Название"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "catalog__genres"
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")
        ordering = ("-created_at",)


class Author(BaseModel):
    full_name = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name=_("ФИО"))

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "catalog__authors"
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        ordering = ("-created_at",)


class Book(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Название"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Описание"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Слаг"))
    genres = models.ManyToManyField("catalog.Genre", related_name="books", verbose_name=_("Жанры"))
    authors = models.ManyToManyField("catalog.Author", related_name="books", verbose_name=_("Авторы"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "catalog__books"
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ("-created_at",)


class Review(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, null=False, blank=False, related_name="reviews")
    book = models.ForeignKey("catalog.Book", on_delete=models.CASCADE, null=False, blank=False, related_name="reviews")
    review = models.TextField(null=True, blank=True, verbose_name=_("Отзыв"))
    rating = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_("Рейтинг от (1 до 5)"),
        validators=[
            MaxValueValidator(5, message=_("Значение должно быть не больше 5.")),
            MinValueValidator(1, message=_("Значение должно быть не меньше 1.")),
        ],
    )

    def __str__(self):
        return self.review

    class Meta:
        db_table = "catalog__reviews"
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ("-created_at",)
