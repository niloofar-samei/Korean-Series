from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    released_year = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=200)

    def __str__(self):
        return self.actor_name


class Actress(models.Model):
    Actress_name = models.CharField(max_length=200)

    def __str__(self):
        return self.actress_name
