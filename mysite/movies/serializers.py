from rest_framework import serializers
from .models import MoviesData

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData
        fields = ['id', 'name', 'duration', 'rating', 'category']