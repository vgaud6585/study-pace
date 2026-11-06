
from django.db import models


class AppLanguage(models.Model):
    """
    Stores programming and markup languages.

    Examples:
    HTML, CSS, JavaScript, Python, Java etc.
    """

    # Language name (must be unique)
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter language name, e.g. HTML, CSS, Python."
    )

    # Short information about the language
    description = models.TextField(
        blank=True,
        help_text="Write a short introduction about this language."
    )

    # Automatically save creation and update dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "App Language"
        verbose_name_plural = "App Languages"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AppContent(models.Model):
    """
    Stores learning content, code examples and complete code.

    Every content belongs to one AppLanguage.
    """

    # Connect content with its programming language
    language = models.ForeignKey(
        AppLanguage,
        on_delete=models.PROTECT,
        related_name="contents",
        help_text="Select the language for this content."
    )

    # Topic heading
    heading = models.CharField(
        max_length=200,
        help_text="Example: CSS Flexbox, HTML Forms."
    )

    # Explanation of the topic
    description = models.TextField(
        blank=True,
        help_text="Explain how this code or concept works."
    )

    # Small code examples for quick review
    code_snippets = models.TextField(
        blank=True,
        help_text="Small code examples for quick revision."
    )

    # Complete code for testing and understanding
    code_box = models.TextField(
        blank=True,
        help_text="Write complete code here for practical testing."
    )

    # Automatically save creation and update dates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "App Content"
        verbose_name_plural = "App Contents"
        ordering = ["language", "heading"]

        # Avoid duplicate headings within the same language
        constraints = [
            models.UniqueConstraint(
                fields=["language", "heading"],
                name="unique_heading_per_language"
            )
        ]

    def __str__(self):
        return f"{self.language.name} - {self.heading}"
