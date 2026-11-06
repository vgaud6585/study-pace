
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import AppLanguage, AppContent
from .forms import AppLanguageForm, AppContentForm


# ==================================================
# DASHBOARD
# ==================================================

def dashboard(request):

    context = {
        "total_languages": AppLanguage.objects.count(),

        "total_contents": AppContent.objects.count(),

        "recent_contents": (
            AppContent.objects
            .select_related("language")
            .order_by("-created_at")[:5]
        ),

        "languages": (
            AppLanguage.objects
            .order_by("name")[:6]
        ),
    }

    return render(
        request,
        "StudyPlace/dashboard.html",
        context
    )


# ==================================================
# LANGUAGE: LIST / SEARCH
# ==================================================

def language_list(request):

    query = request.GET.get("q", "").strip()

    languages = AppLanguage.objects.all()

    if query:
        languages = languages.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    languages = languages.order_by("name")

    context = {
        "languages": languages,
        "query": query,
    }

    return render(
        request,
        "StudyPlace/language_list.html",
        context
    )


# ==================================================
# LANGUAGE: CREATE
# ==================================================

def language_create(request):

    form = AppLanguageForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Language created successfully!"
            )

            return redirect("StudyPlace:language_list")

        messages.error(
            request,
            "Please correct the errors below."
        )

    return render(
        request,
        "StudyPlace/language_form.html",
        {
            "form": form,
            "title": "Add Language",
        }
    )


# ==================================================
# LANGUAGE: EDIT
# ==================================================

def language_edit(request, pk):

    language = get_object_or_404(
        AppLanguage,
        pk=pk
    )

    form = AppLanguageForm(
        request.POST if request.method == "POST" else None,
        instance=language
    )

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Language updated successfully!"
            )

            return redirect("StudyPlace:language_list")

        messages.error(
            request,
            "Please correct the errors below."
        )

    return render(
        request,
        "StudyPlace/language_form.html",
        {
            "form": form,
            "title": "Edit Language",
            "language": language,
        }
    )


# ==================================================
# LANGUAGE: DELETE
# ==================================================

def language_delete(request, pk):

    language = get_object_or_404(
        AppLanguage,
        pk=pk
    )

    if request.method == "POST":

        # Check whether language contains contents
        if language.contents.exists():

            messages.error(
                request,
                "This language contains saved contents. "
                "Delete or move those contents first."
            )

            return redirect("StudyPlace:language_list")

        language.delete()

        messages.success(
            request,
            "Language deleted successfully!"
        )

        return redirect("StudyPlace:language_list")

    return render(
        request,
        "StudyPlace/language_confirm_delete.html",
        {
            "language": language,
        }
    )


# ==================================================
# CONTENT: LIST / SEARCH / FILTER
# ==================================================

def content_list(request):

    query = request.GET.get("q", "").strip()

    language_id = request.GET.get("language", "").strip()

    contents = (
        AppContent.objects
        .select_related("language")
        .all()
    )

    # Search
    if query:

        contents = contents.filter(
            Q(heading__icontains=query) |
            Q(description__icontains=query) |
            Q(code_snippets__icontains=query) |
            Q(code_box__icontains=query) |
            Q(language__name__icontains=query)
        )

    # Language filter
    if language_id:

        contents = contents.filter(
            language_id=language_id
        )

    contents = contents.order_by("-created_at")

    context = {
        "contents": contents,

        "languages": AppLanguage.objects.order_by("name"),

        "query": query,

        "selected_language": language_id,
    }

    return render(
        request,
        "StudyPlace/content_list.html",
        context
    )


# ==================================================
# CONTENT: DETAIL
# ==================================================

def content_detail(request, pk):

    content = get_object_or_404(
        AppContent.objects.select_related("language"),
        pk=pk
    )

    return render(
        request,
        "StudyPlace/content_detail.html",
        {
            "content": content,
        }
    )


# ==================================================
# CONTENT: CREATE
# ==================================================

def content_create(request):

    form = AppContentForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST":

        if form.is_valid():

            content = form.save()

            messages.success(
                request,
                "Content created successfully!"
            )

            return redirect(
                "StudyPlace:content_detail",
                pk=content.pk
            )

        messages.error(
            request,
            "Please correct the errors below."
        )

    return render(
        request,
        "StudyPlace/content_form.html",
        {
            "form": form,
            "title": "Add New Content",
        }
    )


# ==================================================
# CONTENT: EDIT
# ==================================================

def content_edit(request, pk):

    content = get_object_or_404(
        AppContent,
        pk=pk
    )

    form = AppContentForm(
        request.POST if request.method == "POST" else None,
        instance=content
    )

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Content updated successfully!"
            )

            return redirect(
                "StudyPlace:content_detail",
                pk=content.pk
            )

        messages.error(
            request,
            "Please correct the errors below."
        )

    return render(
        request,
        "StudyPlace/content_form.html",
        {
            "form": form,
            "title": "Edit Content",
            "content": content,
        }
    )


# ==================================================
# CONTENT: DELETE
# ==================================================

def content_delete(request, pk):

    content = get_object_or_404(
        AppContent,
        pk=pk
    )

    if request.method == "POST":

        content.delete()

        messages.success(
            request,
            "Content deleted successfully!"
        )

        return redirect("StudyPlace:content_list")

    return render(
        request,
        "StudyPlace/content_confirm_delete.html",
        {
            "content": content,
        }
    )
