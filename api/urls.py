from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from api import views
from .views import MovieSearch, SearchByRating


urlpatterns = [
    path('movie/', views.movie_api),
    path('movie-search/', MovieSearch.as_view()),
    path('movie-search-rating/', SearchByRating.as_view()),

]
