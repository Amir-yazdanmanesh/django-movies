import re
from django.http import JsonResponse
from .models import Movie
from .serializers import ListMoviesSerializer

def movies_list(request):
   movies = Movie.objects.all()
   serializer = ListMoviesSerializer(movies,many=True)
   return JsonResponse({'movies':serializer.data},safe=False)