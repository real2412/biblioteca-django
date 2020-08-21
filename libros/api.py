from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView,
)
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
#from rest_framework.pagination import PageNumberPagination
#from rest_framework.response import Response
from django.db.models import Q, Count, F, Value, IntegerField
from .models import (
    Autor,
    Categoria,
    Libro
)
from .serializers import (
    AutorSerializer,
    AutorRetrieveSerializer,
    CategoriaSerializer,
    LibroSerializer,
    LibroRetrieveSerializer
)

#from django.core.exceptions import ObjectDoesNotExist
#from rest_framework.exceptions import NotFound
#import datetime

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class CategoriaList(ListAPIView):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer
  #  authentication_classes = [IsAuthenticated] )

class AutorListCreate(ListCreateAPIView):
  #queryset = Autor.objects.all()
  permission_classes = [IsAuthenticated|ReadOnly]
  serializer_class = AutorSerializer
  def get_queryset(self):
        return Autor.objects.all().order_by('apellido')

class AutorRetrieve(RetrieveAPIView):
  queryset = Autor.objects.all()
  serializer_class = AutorRetrieveSerializer
  lookup_field = 'id'

class LibroListCreate(ListCreateAPIView):
  #queryset = Libro.objects.all()
  permission_classes = [IsAuthenticated|ReadOnly]
  serializer_class = LibroSerializer
  def get_queryset(self):
        queryNombre = self.request.query_params.get('nombre', '')
        queryAutorNombre = self.request.query_params.get('autornombre', '')
        queryAutorApellido = self.request.query_params.get('autorapellido', '')
        return Libro.objects.all().filter(nombre__icontains=queryNombre)\
                                    .filter(Q(autor__nombre__icontains=queryAutorNombre),Q(autor__apellido__icontains=queryAutorApellido))#alues('nombre', 'nombre_editorial', 'autor', 'categoria')
        #Q(nom__icontains=querySearch)|Q(desc__icontains=querySearch)

class LibroRetrieve(RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated|ReadOnly]
  queryset = Libro.objects.all()
  serializer_class = LibroRetrieveSerializer
  lookup_field = 'id'