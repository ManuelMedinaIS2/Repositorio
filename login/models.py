from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nombre = models.CharField(max_length=35)
    Apellido = models.CharField(max_length=35)
    Email = models.CharField(max_length=35)
    Codigo = models.CharField(max_length=8)

    def NombreCompleto(self):
        cadena="{0} {1}"
        return cadena.format(self.Nombre, self.Apellido)
    @property
    def __str__(self):
        return self.NombreCompleto()