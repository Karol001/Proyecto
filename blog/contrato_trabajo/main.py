import os 
import locale
import re
import shutil
from num2words import num2words
from blog.replaceTextWordDoc import replaceTextWordDoc
from datetime import datetime
from blog.config import base_path

def get_name_tipo_empleador(tipo):
    if tipo == '1':
        return 'persona juridica'
    if tipo == '2':
        return 'entidad sin animo de lucro'
    if tipo == '3':
        return 'persona natural'
    
def formatDate(date):
    """Dar formato a fechas.

    Args:
        date: fecha en formato "2019-06-01".

    Returns:
        Retorna la fecha como el siguiente ejemplo:

        "14 del mes junio del año 2019" 
    """
    date = date.split('-')
    date = datetime(int(date[0]), int(date[1]), int(date[2]))
    fecha_string = str(date.day) + " del mes " + date.strftime("%B") + " del año " + str(date.year)
    return fecha_string

def main_juridica(data):
    os.chdir(os.getcwd())
    
    tipo_empleador = get_name_tipo_empleador(data['tipo_empleador'].value())
    salario_letras = num2words(data['salario_empleado'].value(), lang='es_CO')
    salario_letras = salario_letras.upper()
    smlmv_letras = num2words(data['smlmv'].value(), lang='es_CO')
    fecha_contratacion_empleado = formatDate(data['fecha_contratacion_empleado'].value())
    fecha_nacimiento_empleado = formatDate(data['fecha_nacimiento_empleado'].value())

    variablelist = {'var_empleador': data['nombre_empleador'].value(),
                    'var_representante': data['nombre_representante'].value(),
                    'var_cedula_representante': data['cedula_representante'].value(),
                    'var_nit_empleador': data['nit_empleador'].value(),
                    'var_tipo_empleador': tipo_empleador,
                    'var_domicilio_empleador': data['domicilio_empleador'].value(),
                    'var_naturaleza_empleador': data['naturaleza_empleador'].value(),
                    'var_empleado': data['nombres_empleado'].value() + " " + data['apellidos_empleado'].value(),
                    'var_cedula_empleado': data['cedula_empleado'].value(),
                    'var_domicilio_empleado': data['domicilio_empleado'].value(),
                    'var_fecha_lugar_nacimiento': fecha_nacimiento_empleado + " en " + data['lugar_nacimiento_empleado'].value(),
                    'var_cargo_empleado': data['cargo_empleado'].value(),
                    'var_salario_empleado': data['salario_empleado'].value(),
                    'var_smlmv': data['smlmv'].value(),
                    'var_letra': smlmv_letras,
                    'var_salario_letras': salario_letras,
                    'var_fecha_contrato': fecha_contratacion_empleado ,
                    'var_funciones_empleado': data['funciones_empleado'].value(),
                    'var_objeto_social': data['objeto_social_empleador'].value(),
                    }

    doc_template = base_path + "/CONTRATO DE TRABAJO A TÉRMINO INDEFINIDO JURIDICA.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        replaceTextWordDoc(varkey, varval, doc_final)

    return doc_final
    
def main_natural(data):
    os.chdir(os.getcwd())
    
    tipo_empleador = get_name_tipo_empleador(data['tipo_empleador'].value())
    salario_letras = num2words(data['salario_empleado'].value(), lang='es_CO')
    salario_letras = salario_letras.upper()
    smlmv_letras = num2words(data['smlmv'].value(), lang='es_CO')
    fecha_contratacion_empleado = formatDate(data['fecha_contratacion_empleado'].value())
    fecha_nacimiento_empleador = formatDate(data['fecha_nacimiento_empleador'].value())
    fecha_nacimiento_empleado = formatDate(data['fecha_nacimiento_empleado'].value())

    variablelist = {'var_empleador': data['nombre_empleador'].value(),
                    'var_cc_empleador': data['cedula_empleador'].value(),
                    'var_domicilio_empleador': data['domicilio_empleador'].value(),
                    'var_nacimiento_empleador': fecha_nacimiento_empleador + " en " + data['lugar_nacimiento_empleador'].value(),
                    'var_tipo_empleador': tipo_empleador,
                    'var_objeto_social': data['objeto_social_empleador'].value(),
                    'var_naturaleza_empleador': data['naturaleza_empleador'].value(),
                    'var_empleado': data['nombres_empleado'].value() + " " + data['apellidos_empleado'].value(),
                    'var_cedula_empleado': data['cedula_empleado'].value(),
                    'var_domicilio_empleado': data['domicilio_empleado'].value(),
                    'var_fecha_lugar_nacimiento': fecha_nacimiento_empleado + " en " + data['lugar_nacimiento_empleado'].value(),
                    'var_cargo_empleado': data['cargo_empleado'].value(),
                    'var_salario_empleado': data['salario_empleado'].value(),
                    'var_salario_letras': salario_letras,
                    'var_smlmv': data['smlmv'].value(),
                    'var_letra': smlmv_letras,
                    'var_funciones_empleado': data['funciones_empleado'].value(),
                    'var_fecha_contrato': fecha_contratacion_empleado,
              
                    }

    doc_template = base_path + "/CONTRATO DE TRABAJO A TÉRMINO INDEFINIDO NATURAL.docx"
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        replaceTextWordDoc(varkey, varval, doc_final)

    return doc_final