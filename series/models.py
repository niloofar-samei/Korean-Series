from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    released_year = models.IntegerField(max_length=200)

    def __str__(self):
        return self.movie_name
