from django.db import models

class Movie(models.Model):
    """
        Movie model to store information
        related to movie.
    """
    title = models.CharField(max_length=120)
    released_year = models.IntegerField(default=0000)
    rating = models.FloatField(default=0000)
    movie_id = models.CharField(max_length=30, unique=True)
    genres = models.CharField(max_length=120)

    def __str__(self):
        return self.title