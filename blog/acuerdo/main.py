import os 
import locale
import calendar
import re
import shutil
from datetime import datetime
from blog.acuerdo.ReplaceWord import ReplaceWord
from num2words import num2words
from datetime import datetime
from blog.config import base_path

def establecerFecha(date):
    date= date.split('-')
    date = datetime(int(date[0]), int(date[1]), int(date[2]))
    fecha = str(date.day) + " del mes " + date.strftime('%B') + " del año " + str(date.year)
    return fecha

def main_natural(camposn):
    
    os.chdir(os.getcwd())
    
    Nombre_natural = camposn['Nombre_natural'].value()
    Cedula_natural= camposn['Cedula_natural'].value()
    Razon_social_titular = camposn['Razon_social_titular'].value()
    Sociedadt = camposn['Sociedadt'].value()
    Nit_titular = camposn['Nit_titular'].value()
    Nombre_representante_receptor = camposn['Nombre_representante_receptor'].value()
    Cedula_representante_receptor = camposn['Cedula_representante_receptor'].value()
    Razon_social_receptor = camposn['Razon_social_receptor'].value()
    Nit_receptor = camposn['Nit_receptor'].value()
    Persona = camposn['Persona'].value()
    Consideracion_adicional = camposn['Consideracion_adicional'].value()
    Salario_en_numeros = camposn['Salario_en_numeros'].value()
    Direccion_titular = camposn['Direccion_titular'].value()
    Telefono_titular = camposn['Telefono_titular'].value()
    Email_titular = camposn['Email_titular'].value()
    Direccion_receptor = camposn['Direccion_receptor'].value()
    Telefono_receptor = camposn['Telefono_receptor'].value()
    Email_receptor = camposn['Email_receptor'].value()
    salario_letras= num2words(Salario_en_numeros, lang='es-CO' ).upper() 
    Fecha_contrato = establecerFecha(camposn['Fecha'].value()) 

    variablelist = {'nombrenetu': Nombre_natural,
                    'cedulanatu': Cedula_natural,
                    'razonsot': Razon_social_titular,
                    'tsociedad': Sociedadt,
                    'nittitular': Nit_titular,
                    'nomrepresentan': Nombre_representante_receptor,
                    'cedularet': Cedula_representante_receptor,
                    'razonsr': Razon_social_receptor,
                    'nitreceptor': Nit_receptor,
                    'tipoper': Persona,
                    'consiadi': Consideracion_adicional,
                    'salmn': Salario_en_numeros,
                    'salm': salario_letras,
                    'diretitular': Direccion_titular,
                    'teletitular': Telefono_titular,
                    'emailtitular': Email_titular,
                    'direreceptor': Direccion_receptor,
                    'telereceptor': Telefono_receptor,
                    'emailreceptor': Email_receptor,
                    'Fechacon': Fecha_contrato,
                    }

    doc_template = base_path + "/ACUERDO DE CONFIDENCIALIDAD Y NO COMPETENCIA_copian.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        ReplaceWord(varkey, varval, doc_final)

    return doc_final

def main(campos):

    os.chdir(os.getcwd())
    
    Nombre_representante_titular = campos['Nombre_representante_titular'].value()
    Cedula_representante_titular = campos['Cedula_representante_titular'].value()
    Razon_social_titular = campos['Razon_social_titular'].value()
    Sociedadt = campos['Sociedadt'].value()
    Nit_titular = campos['Nit_titular'].value()
    Nombre_representante_receptor = campos['Nombre_representante_receptor'].value()
    Cedula_representante_receptor = campos['Cedula_representante_receptor'].value()
    Razon_social_receptor = campos['Razon_social_receptor'].value()
    Nit_receptor = campos['Nit_receptor'].value()
    Persona = campos['Persona'].value()
    Consideracion_adicional = campos['Consideracion_adicional'].value()
    Salario_en_numeros = campos['Salario_en_numeros'].value()
    Direccion_titular = campos['Direccion_titular'].value()
    Telefono_titular = campos['Telefono_titular'].value()
    Email_titular = campos['Email_titular'].value()
    Direccion_receptor = campos['Direccion_receptor'].value()
    Telefono_receptor = campos['Telefono_receptor'].value()
    Email_receptor = campos['Email_receptor'].value()
    Fecha_contrato = establecerFecha(campos['Fecha'].value()) 
    salario_letras= num2words(Salario_en_numeros, lang='es-CO' ).upper() 

    variablelist = {'nomrepresentantet': Nombre_representante_titular,
                    'cedulart': Cedula_representante_titular,
                    'razonsot': Razon_social_titular,
                    'sociedad_t': Sociedadt,
                    'nittitular': Nit_titular,
                    'nomrepresentan': Nombre_representante_receptor,
                    'cedularet': Cedula_representante_receptor,
                    'razonsr': Razon_social_receptor,
                    'nitreceptor': Nit_receptor,
                    'tipoper': Persona,
                    'consiadi': Consideracion_adicional,
                    'salmn': Salario_en_numeros,
                    'salm': salario_letras,
                    'diretitular': Direccion_titular,
                    'teletitular': Telefono_titular,
                    'emailtitular': Email_titular,
                    'direreceptor': Direccion_receptor,
                    'telereceptor': Telefono_receptor,
                    'emailreceptor': Email_receptor,
                    'Fechacon': Fecha_contrato,
                    }

    doc_template = base_path + "/ACUERDO DE CONFIDENCIALIDAD Y NO COMPETENCIA_copia.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        ReplaceWord(varkey, varval, doc_final)

    return doc_final