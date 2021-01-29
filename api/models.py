from django.db import models

# Create your models here.


class MovieDetails(models.Model):
    movie_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    released_year = models.CharField(max_length=500)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    genres = models.CharField(max_length=500)

    def __str__(self):
        return self.title
