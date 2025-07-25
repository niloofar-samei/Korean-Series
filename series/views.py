from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    movie_list = Movie.objects.all()
    return render(request, "series/index.html", {"movie_list": movie_list})
