from django.urls import path, re_path

from . import api
from . import views

from django.contrib.auth.decorators import permission_required, login_required

urlpatterns = [
    #path('inicio', views.inicio, name='finanzas-inicio'),
    path("list_categorias", api.CategoriaList.as_view(), name="list-categorias"),
    path("list_create_autores", api.AutorListCreate.as_view(), name="list-create-autores"),
    path("retrieve_autor/<int:id>", api.AutorRetrieve.as_view(), name="retrieve-autor"),
    path("list_create_libros", api.LibroListCreate.as_view(), name="list-create-libros"),
    path("retrieve_libro/<int:id>", api.LibroRetrieve.as_view(), name="retrieve-libro"),
]
