from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    movie_list = Movie.objects.all()
    return render(request, "series/index.html", {"movie_list": movie_list})


def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    actor = movie.actor_set.all()
    actress = movie.actress_set.all()
    return render(
        request,
        "series/movie.html",
        {"movie": movie, "actor": actor, "actress": actress},
    )


def new(request):
    if request.method == "POST":
        new_movie = request.POST.get("movie")
        new_year = request.POST.get("year")
        actress_name = request.POST.get("actress")
        actor_name = request.POST.get("actor")
        Movie.objects.create(movie_name=new_movie, released_year=new_year)
        selected_movie = Movie.objects.get(movie_name=new_movie)
        print(selected_movie.actress_set.all())
        selected_movie.actress_set.create(actress_name=actress_name)
    return render(request, "series/new.html")
