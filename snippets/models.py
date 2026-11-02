
from django.db import models


class CodeSnippet(models.Model):

    # Code title
    title = models.CharField(max_length=200)

    # Programming language
    language = models.CharField(max_length=50)

    # Code description
    description = models.TextField(blank=True)

    # Actual code
    code = models.TextField()

    # Category
    category = models.CharField(max_length=100, blank=True)

    # Favorite status
    is_favorite = models.BooleanField(default=False)

    # Creation date
    created_at = models.DateTimeField(auto_now_add=True)

    # Last update date
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
