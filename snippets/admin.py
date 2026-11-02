
from django.contrib import admin
from .models import CodeSnippet


@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):

    # Admin list mein kaun se columns dikhenge
    list_display = (
        "title",
        "language",
        "category",
        "is_favorite",
        "created_at",
    )

    # Search functionality
    search_fields = (
        "title",
        "language",
        "description",
        "code",
    )

    # Filter options
    list_filter = (
        "language",
        "category",
        "is_favorite",
    )

    # Read-only fields
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # Latest snippets first
    ordering = ("-created_at",)
