from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.decorators.http import require_POST

from .models import CodeSnippet
from .forms import CodeSnippetForm


# READ + SEARCH
def home(request):
    query = request.GET.get("q", "").strip()

    snippets = CodeSnippet.objects.all().order_by("-created_at")

    if query:
        snippets = snippets.filter(
            Q(title__icontains=query) |
            Q(language__icontains=query) |
            Q(category__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, "snippets/home.html", {
        "snippets": snippets,
        "query": query,
    })


# CREATE
def create_snippet(request):
    if request.method == "POST":
        form = CodeSnippetForm(request.POST)

        if form.is_valid():
            snippet = form.save()
            return redirect("snippet_detail", pk=snippet.pk)
    else:
        form = CodeSnippetForm()

    return render(request, "snippets/snippet_form.html", {
        "form": form,
        "page_title": "Add New Code",
    })


# DETAIL
def snippet_detail(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)

    return render(request, "snippets/detail.html", {
        "snippet": snippet,
    })


# UPDATE
def edit_snippet(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)

    if request.method == "POST":
        form = CodeSnippetForm(request.POST, instance=snippet)

        if form.is_valid():
            form.save()
            return redirect("snippet_detail", pk=snippet.pk)
    else:
        form = CodeSnippetForm(instance=snippet)

    return render(request, "snippets/snippet_form.html", {
        "form": form,
        "page_title": "Edit Code",
        "snippet": snippet,
    })


# DELETE
def delete_snippet(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)

    if request.method == "POST":
        snippet.delete()
        return redirect("home")

    return render(request, "snippets/delete_confirm.html", {
        "snippet": snippet,
    })


# FAVORITE
@require_POST
def toggle_favorite(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)

    snippet.is_favorite = not snippet.is_favorite
    snippet.save(update_fields=["is_favorite"])

    return redirect(request.POST.get("next") or "home")