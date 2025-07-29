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
        the_movie = Movie.objects.get(movie_name=request.POST.get("movie"))
        if not the_movie:
            new_movie = request.POST.get("movie")
            new_year = request.POST.get("year")
            actress_name = request.POST.get("actress")
            actor_name = request.POST.get("actor")
            Movie.objects.create(movie_name=new_movie, released_year=new_year)
            selected_movie = Movie.objects.get(movie_name=new_movie)
            selected_movie.actress_set.create(actress_name=actress_name)
            selected_movie.actor_set.create(actor_name=actor_name)
            return render(request, "series/new.html")
        else:
            print("we had it")
            return render(request, "series/new.html")
    if request.method == "GET":
        return render(request, "series/new.html")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
