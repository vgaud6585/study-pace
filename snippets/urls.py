from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("add/", views.create_snippet, name="create_snippet"),

    path("snippet/<int:pk>/", views.snippet_detail,
         name="snippet_detail"),

    path("edit/<int:pk>/", views.edit_snippet,
         name="edit_snippet"),

    path("delete/<int:pk>/", views.delete_snippet,
         name="delete_snippet"),

    path("favorite/<int:pk>/", views.toggle_favorite,
         name="toggle_favorite"),
]