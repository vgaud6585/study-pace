
from django import forms
from .models import AppLanguage, AppContent


class AppLanguageForm(forms.ModelForm):

    class Meta:
        model = AppLanguage
        fields = ["name", "description"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter language name"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "About this language",
                "rows": 4
            }),
        }


class AppContentForm(forms.ModelForm):

    class Meta:
        model = AppContent
        fields = [
            "language",
            "heading",
            "description",
            "code_snippets",
            "code_box",
        ]

        widgets = {
            "language": forms.Select(attrs={
                "class": "form-control"
            }),
            "heading": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter topic heading"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Explain this topic"
            }),
            "code_snippets": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Small code snippets"
            }),
            "code_box": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 12,
                "placeholder": "Write complete code here"
            }),
        }
