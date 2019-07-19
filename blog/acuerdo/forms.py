from django import forms

from blog.acuerdo.models import Document_Acuerdo_Confidencialidad


class AcuerdoForm_natural(forms.ModelForm):
    class Meta:
        model = Document_Acuerdo_Confidencialidad
        fields = [
            'Nombre_natural',
            'Cedula_natural',
            'Razon_social_titular',
            'Sociedadt',
            'Nit_titular',
            'Nombre_representante_receptor',
            'Cedula_representante_receptor',
            'Razon_social_receptor',
            'Nit_receptor',
            'Persona',
            'Consideracion_adicional',
            'Salario_en_numeros',
            'Direccion_titular',
            'Telefono_titular',
            'Email_titular',
            'Direccion_receptor',
            'Telefono_receptor',
            'Email_receptor',
            'Fecha',
            
        ]

        labels = {
            'Nombre_natural': 'Nombre de persona natural',
            'Cedula_natural': 'Cédula persona natural',
            'Razon_social_titular': 'Razón social de la persona jurídica titular',
            'Sociedadt': 'Tipo de sociedad',
            'Nit_titular': 'NIT de EL TITULAR',
            'Nombre_representante_receptor': 'Nombre del representante legal receptor ',
            'Cedula_representante_receptor': 'Cédula de representante legal receptor',
            'Razon_social_receptor': 'Razón social de la persona jurídica receptor',
            'Nit_receptor': 'NIT de EL RECEPTOR',
            'Persona': 'EL TITULAR es una persona ',
            'Consideracion_adicional': 'Consideración adicional que se considera importante' ,
            'Salario_en_numeros' : 'Salarios Mínimos Legales Mensuales Vigentes',
            'Direccion_titular': 'Dirección del titular',
            'Telefono_titular': 'Teléfono del titular',
            'Email_titular': 'E-mail del titular',
            'Direccion_receptor': 'Dirección del receptor',
            'Telefono_receptor': 'Teléfono del receptor',
            'Email_receptor': 'E-mail del receptor',
            'Fecha': 'Fecha de celebración de contrato'
            

        }

        widgets = {
            'Nombre_natural': forms.TextInput(attrs={'class': 'form-control'}),
            'Cedula_natural': forms.TextInput(attrs={'class': 'form-control'}),
            'Razon_social_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Sociedadt': forms.TextInput(attrs={'class': 'form-control'}),
            'Nit_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre_representante_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Cedula_representante_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Razon_social_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Nit_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Persona': forms.TextInput(attrs={'class': 'form-control'}),
            'Consideracion_adicional': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'Salario_en_numeros': forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Email_titular': forms.EmailInput(attrs={'class': 'form-control'}),
            'Direccion_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Email_receptor': forms.EmailInput(attrs={'class': 'form-control'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
            
        }



class AcuerdoForm(forms.ModelForm):
    class Meta:
        model = Document_Acuerdo_Confidencialidad
        fields = [
            'Nombre_representante_titular',
            'Cedula_representante_titular',
            'Razon_social_titular',
            'Sociedadt',
            'Nit_titular',
            'Nombre_representante_receptor',
            'Cedula_representante_receptor',
            'Razon_social_receptor',
            'Nit_receptor',
            'Persona',
            'Consideracion_adicional',
            'Salario_en_numeros',
            'Direccion_titular',
            'Telefono_titular',
            'Email_titular',
            'Direccion_receptor',
            'Telefono_receptor',
            'Email_receptor',
            'Fecha',
        ]

        labels = {
            'Nombre_representante_titular': 'Nombre de representante legal titular',
            'Cedula_representante_titular': 'Cédula de representante legal titular',
            'Razon_social_titular': 'Razón social de la persona jurídica titular',
            'Sociedadt': 'Tipo de sociedad',
            'Nit_titular': 'NIT de EL TITULAR',
            'Nombre_representante_receptor': 'Nombre del representante legal receptor ',
            'Cedula_representante_receptor': 'Cédula de representante legal receptor',
            'Razon_social_receptor': 'Razón social de la persona jurídica receptor',
            'Nit_receptor': 'NIT de EL RECEPTOR',
            'Persona': 'EL TITULAR es una persona ',
            'Consideracion_adicional': 'Consideración adicional que se considera importante' ,
            'Salario_en_numeros' : 'Salarios Mínimos Legales Mensuales Vigentes',
            'Direccion_titular': 'Dirección del titular',
            'Telefono_titular': 'Teléfono del titular',
            'Email_titular': 'E-mail del titular',
            'Direccion_receptor': 'Dirección del receptor',
            'Telefono_receptor': 'Teléfono del receptor',
            'Email_receptor': 'E-mail del receptor',
            'Fecha': 'Fecha de celebración de contrato',
            

        }

        widgets = {
            'Nombre_representante_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Cedula_representante_titular': forms.TextInput(attrs={'class': 'form-control'}), 
            'Razon_social_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Sociedadt': forms.TextInput(attrs={'class': 'form-control'}),
            'Nit_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Nombre_representante_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Cedula_representante_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Razon_social_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Nit_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Persona': forms.TextInput(attrs={'class': 'form-control'}),
            'Consideracion_adicional': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'Salario_en_numeros': forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'Email_titular': forms.EmailInput(attrs={'class': 'form-control'}),
            'Direccion_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono_receptor': forms.TextInput(attrs={'class': 'form-control'}),
            'Email_receptor': forms.EmailInput(attrs={'class': 'form-control'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date'}),
            
        }

