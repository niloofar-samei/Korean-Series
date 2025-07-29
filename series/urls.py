from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<int:movie_id>/", views.movie, name="movie"),
    path("new/", views.new, name="new"),
    path("delete/<int:movie_id>", views.delete, name="delete"),
]
