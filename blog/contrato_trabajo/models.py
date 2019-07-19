from django.db import models

class TipoEmpleador(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
        
class ContratoTrabajo(models.Model):
    nombres_empleado = models.CharField(max_length=50)
    apellidos_empleado= models.CharField(max_length=100)
    cedula_empleado = models.CharField(max_length=11)
    cedula_empleador = models.CharField(max_length=11)
    domicilio_empleado = models.CharField(max_length=50)
    fecha_nacimiento_empleado = models.DateField()
    fecha_nacimiento_empleador = models.DateField()
    lugar_nacimiento_empleado = models.CharField(max_length=50)
    lugar_nacimiento_empleador = models.CharField(max_length=50)
    cargo_empleado = models.CharField(max_length=40)
    fecha_contratacion_empleado = models.DateField()
    salario_empleado = models.FloatField()
    smlmv = models.IntegerField()
    smlmv_letra = models.CharField(max_length=50)
    salario_letras_empleado = models.CharField(max_length=100)
    nombre_empleador = models.CharField(max_length=50)
    nombre_representante = models.CharField(max_length=50)
    cedula_representante = models.CharField(max_length=11)
    nit_empleador = models.CharField(max_length=20)
    domicilio_empleador = models.CharField(max_length=50)
    naturaleza_empleador = models.CharField(max_length=50)
    objeto_social_empleador = models.CharField(max_length=50)
    funciones_empleado = models.TextField()
    tipo_empleador = models.ForeignKey(TipoEmpleador, null=True, blank=True, on_delete= models.CASCADE)