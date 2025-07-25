from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    released_year = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_name


class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.actor_name


class Actress(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actress_name = models.CharField(max_length=200)

    def __str__(self):
        return self.actress_name
