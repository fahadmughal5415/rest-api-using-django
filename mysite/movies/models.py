from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class MoviesData(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length=200, default='movies')
    image = models.ImageField(upload_to='media', default='images/movvies/noimg.jpg')