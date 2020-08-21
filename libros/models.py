from django.db import models

# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=120, verbose_name="Nombre")
  def __str__(self):
    return self.nombre

class Autor(models.Model):
  nombre = models.CharField(max_length=120, verbose_name="Nombre")
  apellido = models.CharField(max_length=120, verbose_name="Apellido")
  edad = models.IntegerField( null=True, blank=True, verbose_name="Edad")
  def __str__(self):
    return self.nombre

  def get_nombre_completo(self):
    return self.nombre + ' ' + self.apellido
        
  nombre_completo = property(get_nombre_completo)

class Libro(models.Model):
  nombre = models.CharField(max_length=120, verbose_name="Nombre")
  nombre_editorial = models.CharField(max_length=120, null=True, blank=True, verbose_name="Nombre Editorial")
  autor = models.ForeignKey(Autor, related_name="autor_libro",
                              verbose_name="Autor", on_delete=models.CASCADE)
  categoria = models.ForeignKey(Categoria, related_name="categoria_libro",
                              verbose_name="Categoria", on_delete=models.CASCADE)
  def __str__(self):
    return self.nombre
