from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MoviesSerializer
from .models import MoviesData

# Create your views here.

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MoviesSerializer
