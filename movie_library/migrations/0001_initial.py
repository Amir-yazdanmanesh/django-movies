# Generated by Django 4.1.1 on 2022-09-27 20:27

import datetime
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('A', 'Action'), ('C', 'Comedy'), ('D', 'Drama'), ('C', 'Fantasy'), ('C', 'Horror'), ('C', 'Mystery'), ('C', 'Romance'), ('C', 'Thriller'), ('0', 'OTHER')], default='other', max_length=1)),
                ('year_of_release', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('age_rating', models.CharField(choices=[('G', 'General Audiences'), ('PG', 'Parental Guidance Suggested'), ('PG-13', 'Inappropriate for Children Under 13'), ('R', 'Restricted'), ('NC-17', 'Adults Only')], default='GENERAL AUDIENCE', max_length=5)),
                ('average_rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('movie_img', models.ImageField(default=None, upload_to='files/covers')),
            ],
            options={
                'ordering': ['-year_of_release'],
            },
        ),
    ]
