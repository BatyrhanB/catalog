from django.contrib import admin

from catalog.models import Genre, Author, Book, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = [
        "name",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["name", "created_at", "updated_at"]
    list_filter = ["is_deleted", "created_at", "updated_at"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["full_name", "created_at", "updated_at"]
    search_fields = [
        "full_name",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["full_name", "created_at", "updated_at"]
    list_filter = ["is_deleted", "created_at", "updated_at"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = [
        "name",
        "description",
        "slug",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["name", "slug", "description", "genres", "authors", "created_at", "updated_at"]
    list_filter = ["genres", "authors", "is_deleted", "created_at", "updated_at"]
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["book", "rating", "created_at", "updated_at"]
    search_fields = [
        "book",
        "review",
    ]
    readonly_fields = [
        "id",
        "created_at",
        "updated_at",
    ]
    ordering = ["-created_at"]
    list_per_page = 25
    fields = ["book", "review", "rating", "created_at", "updated_at"]
    list_filter = ["book", "rating", "is_deleted", "created_at", "updated_at"]
