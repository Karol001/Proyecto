from django import forms
from blog.contrato_trabajo.models import ContratoTrabajo


class ContratoJuridicoForm(forms.ModelForm):
    class Meta:
        model = ContratoTrabajo

        fields = [
            'nombres_empleado',
            'apellidos_empleado',
            'cedula_empleado',
            'domicilio_empleado',
            'fecha_nacimiento_empleado',
            'lugar_nacimiento_empleado',
            'cargo_empleado',
            'fecha_contratacion_empleado',
            'salario_empleado',
            'smlmv',
            'nombre_empleador',
            'nombre_representante',
            'cedula_representante',
            'nit_empleador',
            'domicilio_empleador',
            'naturaleza_empleador',
            'tipo_empleador',
            'objeto_social_empleador',
            'funciones_empleado',
        ]

        labels = {
            'nombres_empleado': 'Nombres del empleado',
            'apellidos_empleado': 'Apellidos del empleado',
            'cedula_empleado': 'Cedula del empleado',
            'domicilio_empleado': 'Domicilio del empleado',
            'fecha_nacimiento_empleado': 'Fecha de nacimiento del empleado',
            'lugar_nacimiento_empleado': 'Lugar de nacimiento del empleado',
            'cargo_empleado': 'Cargo del empleado',
            'fecha_contratacion_empleado': 'Fecha tentativa de contratacion',
            'salario_empleado': 'Salario del empleado',
            'smlmv': 'Suma de cláusula penal',
            'nombre_empleador': 'Nombre del empleador',
            'nombre_representante': 'Nombre de representante legal',
            'cedula_representante': 'Cedula de representante legal',
            'nit_empleador': 'Nit empleador',
            'domicilio_empleador': 'Domicilio empleador',
            'naturaleza_empleador': 'Naturaleza empleador',
            'tipo_empleador': 'Tipo de empleador',
            'objeto_social_empleador': 'Objeto social del empleador',
            'funciones_empleado': 'Funciones propias del cargo que se contrata',
        }

        widgets = {
            'nombres_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'apellidos_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'cedula_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'domicilio_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'fecha_nacimiento_empleado': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'required': 'true'
                }),

            'lugar_nacimiento_empleado': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'cargo_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'fecha_contratacion_empleado': forms.DateInput(
                attrs={
                    'class': 'form-control datepicker',
                    'type': 'date',
                    'required': 'true'
                }),

            'salario_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'smlmv': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'nombre_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'nombre_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'cedula_representante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'nit_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'domicilio_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'naturaleza_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'objeto_social_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'tipo_empleador': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                }),

            'funciones_empleado': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': "2",
                    'required': 'true'
                })
        }

class ContratoNaturalForm(forms.ModelForm):
    class Meta:
        model = ContratoTrabajo

        fields = [
            'nombre_empleador',
            'cedula_empleador',
            'domicilio_empleador',
            'fecha_nacimiento_empleador',
            'lugar_nacimiento_empleador',
            'tipo_empleador',
            'objeto_social_empleador',
            'naturaleza_empleador',

            'nombres_empleado',
            'apellidos_empleado',
            'cedula_empleado',
            'domicilio_empleado',
            'fecha_nacimiento_empleado',
            'lugar_nacimiento_empleado',
            'cargo_empleado',
            'salario_empleado',
            'smlmv',
            'fecha_contratacion_empleado',
            'funciones_empleado',
        ]

        labels = {
            'nombre_empleador': 'Nombre completo del empleador',
            'cedula_empleador': 'Cedula del empleador',
            'domicilio_empleador': 'Domicilio del empleador',
            'fecha_nacimiento_empleador': 'Fecha de nacimiento del empleador',
            'lugar_nacimiento_empleador': 'Lugar de nacimiento del empleador',
            'tipo_empleador': 'Tipo de empleador',
            'objeto_social_empleador': 'Objeto social del empleador',
            'naturaleza_empleador': 'Naturaleza del empleador',

            'nombres_empleado': 'Nombres del empleado',
            'apellidos_empleado': 'Apellidos del empleado',
            'cedula_empleado': 'Cedula del empleado',
            'domicilio_empleado': 'Domicilio del empleado',
            'fecha_nacimiento_empleado': 'Fecha de nacimiento del empleado',
            'lugar_nacimiento_empleado': 'Lugar de nacimiento del empleado',
            'cargo_empleado': 'Cargo del empleado',
            'salario_empleado': 'Salario del empleado',
            'smlmv': 'Suma de cláusula penal',
            'fecha_contratacion_empleado': 'Fecha de contratacion',
            'funciones_empleado': 'Funciones del empleado',
        }

        widgets = {
            'nombre_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'cedula_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'domicilio_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'fecha_nacimiento_empleador': forms.DateInput(
                attrs={
                    'class': 'form-control'
                    , 'type': 'date','required': 'true'
                    }),

            'lugar_nacimiento_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'tipo_empleador': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'objeto_social_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'naturaleza_empleador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'nombres_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'apellidos_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'cedula_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'domicilio_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'fecha_nacimiento_empleado': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                    ,'required': 'true'
                    }),

            'lugar_nacimiento_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'cargo_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'salario_empleado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'smlmv': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true'
                    }),

            'fecha_contratacion_empleado': forms.DateInput(
                attrs={
                    'class': 'form-control'
                    , 'type': 'date','required': 'true'
                    }),

            'funciones_empleado': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'rows': '2',
                    'required': 'true'
                    }),
        }
