
from django import forms
from .models import CodeSnippet


class CodeSnippetForm(forms.ModelForm):

    class Meta:
        model = CodeSnippet

        fields = [
            "title",
            "language",
            "description",
            "code",
            "category",
            "is_favorite",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter code title"
            }),

            "language": forms.TextInput(attrs={
                "placeholder": "e.g. HTML, CSS, Python"
            }),

            "description": forms.Textarea(attrs={
                "placeholder": "Explain what this code does",
                "rows": 3
            }),

            "code": forms.Textarea(attrs={
                "placeholder": "Write or paste your code here",
                "rows": 12
            }),

            "category": forms.TextInput(attrs={
                "placeholder": "e.g. Frontend, Backend"
            }),
        }
