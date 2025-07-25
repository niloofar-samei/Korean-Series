from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor, Actress


def index(request):
    movie_list = Movie.objects.all()
    return render(request, "series/index.html", {"movie_list": movie_list})


def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    actor = movie.actor_set.all()
    actress = movie.actress_set.all()
    print(actor)
    print(actress)
    return render(
        request,
        "series/movie.html",
        {"movie": movie, "actor": actor, "actress": actress},
    )
