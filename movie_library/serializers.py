from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import Movie

class ListMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','movie_name','genre']