from django.db import models

class Tipo(models.Model):
 tipo= models.CharField(max_length=50)

 def __str__(self):
    return '{}'.format(self.tipo)


class Anos_meses(models.Model):
    am = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.am)


class Document_contrato(models.Model):
     Razon_social_natural = models.CharField(max_length=70)
     Cedula_contratante_natural = models.IntegerField()
     Ciudad_contratante_natural = models.CharField(max_length=70)
     Fecha_nacimiento_contratante_natural= models.DateField()
     Lugar_nacimiento_contratante_natural = models.CharField(max_length=70)
     Razon_social_juridica = models.CharField(max_length=70)
     Nit_juridica= models.IntegerField()
     Nombre_representante= models.CharField(max_length=70)
     Cedula_representate= models.IntegerField()
     Razon_social_juridica_contratista = models.CharField(max_length=70)
     Nit_juridica_contratista = models.CharField(max_length=70)
     Nombre_representante_contratista = models.CharField(max_length=70)
     Cedula_representate_contratista = models.CharField(max_length=70)
     Nombre_natural= models.CharField(max_length=70)
     Cedula_contratista= models.IntegerField()
     Ciudad_contratista= models.CharField(max_length=100)
     Fecha_nacimiento_contratista= models.DateField()
     Lugar_nacimiento_contratista= models.CharField(max_length=100)
     Actividad_profesional_contratista= models.CharField(max_length=100)
     Objeto_social_contratista= models.CharField(max_length=100)
     Objeto_social_contratante= models.CharField(max_length=100)
     Dedicacion_profesional_natural= models.CharField(max_length=100)
     Finalidad= models.CharField(max_length=100)
     Servicio_manera_general= models.CharField(max_length=100)
     Servicio_prestado_contratista= models.CharField(max_length=255)
     Paragrafo_primero= models.BooleanField()
     Contraprestacion_letras= models.IntegerField()
     Contraprestacion_numeros= models.CharField(max_length=255)
     Plazo_sugerido_dias= models.IntegerField()
     Plazo_sugerido_letras= models.IntegerField()
     Banco= models.CharField(max_length=50)
     Tipo_cuenta= models.CharField(max_length=50)
     Numero_cuenta= models.IntegerField()
     Nombre_titular= models.CharField(max_length=50)
     Cedula_titular= models.IntegerField()
     Duracion_letras= models.CharField(max_length=50)
     Duracion_numeros= models.IntegerField()
     Dias_prueba_letras= models.CharField(max_length=20)
     Dias_prueba_numeros= models.IntegerField()
     Paragrafo_prueba_opcional=models.CharField(max_length=20)
     Fecha_prueba=models.IntegerField()
     Direccion_Fisica_contratante=models.CharField(max_length=40)
     Correo_electronico_contratante=models.EmailField()
     Tipo_con = models.ForeignKey(Tipo, null=True, blank=True, on_delete= models.CASCADE)
     Anos_meses = models.ForeignKey(Anos_meses, null=True, blank=True, on_delete= models.CASCADE)


