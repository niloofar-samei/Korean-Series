from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import F
from .models import Movie


def index(request):
    movie_list = Movie.objects.all().order_by("-voteup")
    return render(request, "series/index.html", {"movie_list": movie_list})


def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    actor = movie.actor_set.all()
    actress = movie.actress_set.all()
    print("-------")
    print(actress)
    return render(
        request,
        "series/movie.html",
        {"movie": movie, "actor": actor, "actress": actress},
    )


def new(request):
    if request.method == "POST":
        existing_movie = Movie.objects.filter(
            movie_name=request.POST.get("movie")
        ).first()

        if existing_movie:
            return render(request, "series/new.html")
        else:
            try:
                new_movie = request.POST.get("movie")
                new_year = request.POST.get("year")
                actress_name = request.POST.get("actress")
                actor_name = request.POST.get("actor")
                movie_image = request.FILES.got("movie_image")
                actress_image = request.FILES.get("actress_image")
                actor_image = request.FILES.get("actor_image")
                new_movie = Movie.objects.create(
                    movie_name=new_movie,
                    released_year=new_year,
                    movie_image=movie_image,
                )
                new_movie.actress_set.create(
                    actress_name=actress_name, actress_image=actress_image
                )
                new_movie.actor_set.create(
                    actor_name=actor_name, actor_image=actor_image
                )
                messages.success(request, f"Movie '{new_movie}' created successfully.")
                return redirect("new")

            except Exception as e:
                print("Error while saving:", e)
                messages.error(request, "You got error.")
                return redirect(new)

    return render(request, "series/new.html")


def delete(request, movie_id):
    print(movie_id)
    selected_movie = Movie.objects.get(pk=movie_id)
    selected_movie.delete()
    return redirect("index")


def voteup(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.voteup = F("voteup") + 1
    movie.save()
    return redirect("index")
