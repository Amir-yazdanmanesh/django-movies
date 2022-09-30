from datetime import datetime
from django.db import models

# Create your models here.

from django.db import models
import uuid
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import date
from django.urls import reverse

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENRE_CHOICES = [
        ("A", "Action"),
        ("C", "Comedy"),
        ("D", "Drama"),
        ("C", "Fantasy"),
        ("C", "Horror"),
        ("C", "Mystery"),
        ("C", "Romance"),
        ("C", "Thriller"),
        ("0", "OTHER"),
    ]
    movie_name = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=1, choices=GENRE_CHOICES, default="other")
    year_of_release = models.DateField(("Date"), default=date.today)
    AGE_RATING = [
        ("G", "General Audiences"),
        ("PG", "Parental Guidance Suggested"),
        ("PG-13", "Inappropriate for Children Under 13"),
        ("R", "Restricted"),
        ("NC-17", "Adults Only"),
    ]
    age_rating = models.CharField(
        max_length=5, choices=AGE_RATING, default="GENERAL AUDIENCE")
    average_rating = models.FloatField(
      validators=[MinValueValidator(0.0),MaxValueValidator(10.0)],
    )
    
    movie_img = models.ImageField(upload_to='media/files/covers', null=True, blank=True,default = None)
    
    
    class Meta:
        ordering = ["-year_of_release"]


    def __str__(self):
        return self.movie_name + "-" + self.year_of_release.strftime('%Y')


