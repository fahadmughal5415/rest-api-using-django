from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MoviesSerializer
from .models import MoviesData

# Create your views here.

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MoviesSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(category='action')
    serializer_class = MoviesSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(category='comedy')
    serializer_class = MoviesSerializer

class HorrorViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(category='horror')
    serializer_class = MoviesSerializer
