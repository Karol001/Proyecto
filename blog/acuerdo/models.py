from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator


class persona(models.Model):
    Tipo_persona = models.CharField(max_length=50)

class Sociedad(models.Model):
    Nombre_sociedad = models.CharField(max_length=40)

class Document_Acuerdo_Confidencialidad(models.Model):
    Nombre_natural = models.CharField(max_length=50, null=True)
    Cedula_natural = models.CharField(max_length=50, null=True)
    Nombre_representante_titular = models.CharField(max_length=100)
    Cedula_representante_titular = models.CharField(max_length=12)
    Razon_social_titular = models.CharField(max_length=50)
    Sociedadt = models.CharField(max_length=50)
    Nit_titular = models.CharField (max_length=30)
    Nombre_representante_receptor = models.CharField(max_length=100)
    Cedula_representante_receptor = models.CharField(max_length=12)
    Razon_social_receptor = models.CharField(max_length=50)
    Nit_receptor = models.CharField (max_length=30)
    Persona = models.CharField(max_length=40)
    Consideracion_adicional= models.TextField ()
    Salario = models.CharField(max_length=40)
    Salario_en_numeros = models.DecimalField(max_digits=20,decimal_places=10)
    Direccion_titular= models.CharField (max_length=50)
    Telefono_titular= models.CharField (max_length=30)
    Email_titular= models.EmailField ()
    Direccion_receptor = models.CharField (max_length=50)
    Telefono_receptor = models.CharField (max_length=30)
    Email_receptor= models.EmailField ()
    Fecha= models.DateField()
   