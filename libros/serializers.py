from rest_framework import serializers
from .models import Autor, Categoria, Libro

class AutorSerializer(serializers.ModelSerializer):

  nombre = serializers.CharField(write_only=True)
  edad = serializers.CharField(write_only=True, required=False)

  def create(self, validated_data):

      autor = Autor.objects.create(
          nombre=validated_data['nombre'],
          apellido=validated_data['apellido'],
          edad=validated_data.get('edad', None),
      )
      autor.save()

      return autor


  class Meta:
    model = Autor
    fields = ['id','nombre', 'apellido', 'edad']

class AutorRetrieveSerializer(serializers.ModelSerializer):

  class Meta:
    model = Autor
    fields = ['id','nombre', 'apellido', 'edad']


class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ['id','nombre']


class LibroSerializer(serializers.ModelSerializer):
  #nombre_completo = serializers.ReadOnlyField()
  nombre_completo = serializers.CharField(
        source='autor.nombre_completo',
        read_only=True,
    )

  nombre_editorial = serializers.CharField(write_only=True)

  class Meta:
    model = Libro
    fields = ['id','nombre', 'nombre_editorial','autor','nombre_completo','categoria']


class LibroRetrieveSerializer(serializers.ModelSerializer):
  #nombre_completo = serializers.ReadOnlyField()
  nombre_completo = serializers.CharField(
        source='autor.nombre_completo',
        read_only=True,
    )

  nombre_categoria = serializers.CharField(
        source='categoria.nombre',
        read_only=True,
    )

  nombre_editorial = serializers.CharField(write_only=True)

  class Meta:
    model = Libro
    fields = ['id','nombre', 'nombre_editorial','nombre_categoria','nombre_completo']

  