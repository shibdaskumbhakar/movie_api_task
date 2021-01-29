from rest_framework import serializers
from .models import MovieDetails


class MovieDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieDetails
        fields = ('movie_id', 'title', 'released_year', 'rating', 'genres')
