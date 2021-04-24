from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    

    # quitar paginacion, es para quitar la paginacion de la cnosulta
    # def get_queryset(self):
    # if self.request.GET.get('pagination') == 'none': self.pagination_class = None
    # return super().get_queryset()