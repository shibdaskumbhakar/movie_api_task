from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MovieDetails
from .serializers import MovieDetailsSerializers
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django.http import HttpResponse
import json
from .utils import getdata


# Create your views here.


@api_view(['GET'])
def movie_api(request):
    title = request.data.get('title')
    print(title)
    if title is not None:
        movie = MovieDetails.objects.filter(title=title)
        if MovieDetails.objects.filter(title=title).exists():
            serializer = MovieDetailsSerializers(movie, many=True)
            return Response(serializer.data)
        else:
            data = getdata(title)
            movie_title = data.get('Title')
            released_year = data.get('Year')
            imdbRating = data.get('imdbRating')
            genres = data.get('Genre')
            movie_id = data.get('imdbID')
            movie_details = MovieDetails.objects.create(
                movie_id=movie_id, title=movie_title, released_year=released_year, rating=imdbRating, genres=genres)
            movie_details.save()
            get_movie = MovieDetails.objects.filter(title=title)
            serializer = MovieDetailsSerializers(get_movie, many=True)
            return Response(serializer.data)
    else:
        return Response({"message": "enter a currect movie name."})


class MovieSearch(ListAPIView):
    queryset = MovieDetails.objects.all()
    serializer_class = MovieDetailsSerializers
    filter_backends = [SearchFilter]
    search_fields = ['movie_id', 'rating', 'released_year', 'genres']


class SearchByRating(APIView):
    def get(self, request, format=None):
        rating = request.data.get('rating')
        if rating is not None:
            rating = float(rating)
            movie = MovieDetails.objects.filter(rating=rating)
            serializer = MovieDetailsSerializers(movie, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "plese enter a rating value"})
