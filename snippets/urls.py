
from django.urls import path
from . import views


app_name = "StudyPlace"


urlpatterns = [

    # ==================================
    # DASHBOARD
    # ==================================

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),


    # ==================================
    # LANGUAGE URLS
    # ==================================

    path(
        "languages/",
        views.language_list,
        name="language_list"
    ),

    path(
        "languages/add/",
        views.language_create,
        name="language_create"
    ),

    path(
        "languages/<int:pk>/edit/",
        views.language_edit,
        name="language_edit"
    ),

    path(
        "languages/<int:pk>/delete/",
        views.language_delete,
        name="language_delete"
    ),


    # ==================================
    # CONTENT URLS
    # ==================================

    path(
        "contents/",
        views.content_list,
        name="content_list"
    ),

    path(
        "contents/add/",
        views.content_create,
        name="content_create"
    ),

    path(
        "contents/<int:pk>/",
        views.content_detail,
        name="content_detail"
    ),

    path(
        "contents/<int:pk>/edit/",
        views.content_edit,
        name="content_edit"
    ),

    path(
        "contents/<int:pk>/delete/",
        views.content_delete,
        name="content_delete"
    ),

]
