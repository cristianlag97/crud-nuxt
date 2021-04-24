from rest_framework import serializers
from rest_framework_serializer_extensions.serializers import (
    SerializerExtensionsMixin)
    
from .models import *


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'autor', 'titulo', 'fecha_creacion', 'compras', 'nombre']


    # expandable_fields = {
    #     'autor': (AutorSerializer, { 'many': True }),
    # }

    expandible_fields  =  dict (
        autor = dict (
            serializer = AutorSerializer ,
            read_only = False
    )
)