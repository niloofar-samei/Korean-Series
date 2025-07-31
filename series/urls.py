from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<int:movie_id>/", views.movie, name="movie"),
    path("new/", views.new, name="new"),
    path("new_django_form", views.new_django_form, name="new_django_form"),
    path(
        "new_django_form_movie/",
        views.new_django_form_movie,
        name="new_django_form_movie",
    ),
    path(
        "add_actress-actor/<int:movie_id>/",
        views.add_actress_actor,
        name="add_actress_actor",
    ),
    path("delete/<int:movie_id>", views.delete, name="delete"),
    path("voteup/<int:movie_id>", views.voteup, name="voteup"),
]
