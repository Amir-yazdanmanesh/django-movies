import re
from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Movie
from .serializers import ListMoviesSerializer


def list_movies(request):
    movies = Movie.objects.all()
    serializer = ListMoviesSerializer(movies, many=True, context={'request': request})
    return JsonResponse({'movies': serializer.data}, safe=False)


def postMovies(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'movies/movie.html', {'movie': movie})
    else:
           raise Http404('mMovie does not exist')

def getAllmovies(request):
    movie = Movie.objects.all()
    if movie is not None:
        return render(request, 'moviehunter/index.html', {'movies': movie})
    else:
           raise Http404('mMovie does not exist')
