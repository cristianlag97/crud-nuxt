from rest_framework import serializers
from .models import *


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__alll__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'