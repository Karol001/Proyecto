import os 
import locale
import re
import shutil
from num2words import num2words
from blog.replaceTextWordDoc import replaceTextWordDoc
from datetime import datetime
from blog.config import base_path

def tipocon(tipo):
    if tipo == '2':
        return 'El CONTRATANTE'
    if tipo == '1':
        return 'EL CONTRATISTA'

def Anosomeses(tipo):
    if tipo == '1':
        return 'Años'
    if tipo == '2':
        return 'Meses'

def formatDate(date):
    date = date.split('-')
    date = datetime(int(date[0]), int(date[1]), int(date[2]))
    fecha_string = str(date.day) + " del mes " + date.strftime("%B") + " del año " + str(date.year)
    return fecha_string

def main_JyN(Campojn):
    os.chdir(os.getcwd())
    
    Tipo_con = tipocon(Campojn['Tipo_con'].value())
    Anos_meses= Anosomeses(Campojn['Anos_meses'].value())
    Contraprestacion_letras = num2words(Campojn['Contraprestacion_numeros'].value(), lang='es_CO').upper()
    Plazo_sugerido_letras = num2words(Campojn['Plazo_sugerido_dias'].value(), lang='es_CO').upper()
    Duracion_letras = num2words(Campojn['Duracion_numeros'].value(), lang='es_CO').upper()
    Fecha_nacimiento_contratista = formatDate(Campojn['Fecha_nacimiento_contratista'].value())

    if Campojn['Paragrafo_prueba_opcional'].value() != True:
        paragrafoc = ''
    else:
        paragrafoc = """ PARAGRAFO. No obstante lo anterior, las partes iniciaron un periodo de prueba de diasletras (diasnum) DÍAS contados a partir del fech. Una vez cumplido este término de prueba, empezará a contar el periodo establecido del presente Contrato.\n La finalidad de este periodo de prueba tiene como objetivo delimitar el alcance de los servicios requeridos por EL CONTRANTE y, así, lo aceptan expresamente las partes. """
        Dias_prueba_letras = num2words(Campojn['Dias_prueba_numeros'].value(), lang='es_CO').upper()
        Fecha_prueba = formatDate(Campojn['Fecha_prueba'].value())

    if Campojn['Paragrafo_primero'].value() != True:
        pragrafo_primero = ''
    else:
        pragrafo_primero = 'PARÁGRAFO PRIMERO. Las partes procederán con la realización de una “agenda de trabajo” escrito que hará parte integral del presente Contrato, con miras a cumplir y ejecutar en debida forma las obligaciones acá contenidas.'
    
    variablelist = {'Razonsj': Campojn['Razon_social_juridica'].value(),
                    'Nitperj': Campojn['Nit_juridica'].value(),
                    'Nomrcl': Campojn['Nombre_representante'].value(),
                    'cedulre': Campojn['Cedula_representate'].value(),
                    'Nombre_natural': Campojn['Nombre_natural'].value(),
                    'cedcon': Campojn['Cedula_contratista'].value(),
                    'domicon': Campojn['Ciudad_contratista'].value(),
                    'fechana': Fecha_nacimiento_contratista,
                    'lugarna': Campojn['Lugar_nacimiento_contratista'].value(),
                    'actiprocon': Campojn['Actividad_profesional_contratista'].value(),
                    'objsoj': Campojn['Objeto_social_contratante'].value(),
                    'finalidads': Campojn['Finalidad'].value(),
                    'servigeneral': Campojn['Servicio_manera_general'].value(),
                    'Servicon': Campojn['Servicio_prestado_contratista'].value(),
                    'contraprenum': Campojn['Contraprestacion_numeros'].value(),
                    'contraprestacion': Contraprestacion_letras,
                    'plazonum': Campojn['Plazo_sugerido_dias'].value(),
                    'plazole': Plazo_sugerido_letras,
                    'ccr': Campojn['Banco'].value(),
                    'cuentac': Campojn['Tipo_cuenta'].value(),
                    'numcuenta': Campojn['Numero_cuenta'].value(),
                    'nomtitular': Campojn['Nombre_titular'].value(),
                    'identitular': Campojn['Cedula_titular'].value(),
                    'tipogas': Tipo_con,
                    'duranum': Campojn['Duracion_numeros'].value(),
                    'duraletras': Duracion_letras,
                    'anoomes': Anos_meses,
                    'direfc' : Campojn['Direccion_Fisica_contratante'].value(),
                    'diree' : Campojn['Correo_electronico_contratante'].value(),
                    'paragrafoc' : paragrafoc,
                    'paragraprim': pragrafo_primero,
                    }

    if Campojn['Paragrafo_prueba_opcional'].value() == True:
      
        variablelist['diasnum'] = Campojn['Dias_prueba_numeros'].value()
        variablelist['diasletras'] = Dias_prueba_letras
        variablelist['fech'] = Fecha_prueba

    doc_template = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS JyN.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        replaceTextWordDoc(varkey, varval, doc_final)

    return doc_final

def main_JyJ(Campojj):
    os.chdir(os.getcwd())
    
    Tipo_con = tipocon(Campojj['Tipo_con'].value())
    Anos_meses= Anosomeses(Campojj['Anos_meses'].value())
    Contraprestacion_letras = num2words(Campojj['Contraprestacion_numeros'].value(), lang='es_CO').upper()
    Plazo_sugerido_letras = num2words(Campojj['Plazo_sugerido_dias'].value(), lang='es_CO').upper()
    Duracion_letras = num2words(Campojj['Duracion_numeros'].value(), lang='es_CO').upper()

    if Campojj['Paragrafo_prueba_opcional'].value() != True:
        paragrafoc = ''
    else:
        paragrafoc = """ PARAGRAFO. No obstante lo anterior, las partes iniciaron un periodo de prueba de diasletras (diasnum) DÍAS contados a partir del Fecha_prueba. Una vez cumplido este término de prueba, empezará a contar el periodo establecido del presente Contrato.
                    La finalidad de este periodo de prueba tiene como objetivo delimitar el alcance de los servicios requeridos por EL CONTRANTE y, así, lo aceptan expresamente las partes. """
        Dias_prueba_letras = num2words(Campojj['Dias_prueba_numeros'].value(), lang='es_CO').upper()
        Fecha_prueba = formatDate(Campojj['Fecha_prueba'].value())
    if Campojj['Paragrafo_primero'].value() != True:
        pragrafo_primero = ''
    else:
        pragrafo_primero = 'PARÁGRAFO PRIMERO. Las partes procederán con la realización de una “agenda de trabajo” escrito que hará parte integral del presente Contrato, con miras a cumplir y ejecutar en debida forma las obligaciones acá contenidas.'
    
    variablelist = {'Razonsj': Campojj['Razon_social_juridica'].value(),
                    'Nitperj': Campojj['Nit_juridica'].value(),
                    'Nomrcl': Campojj['Nombre_representante'].value(),
                    'cedulre': Campojj['Cedula_representate'].value(),

                    'razoncte': Campojj['Razon_social_juridica_contratista'].value(),
                    'nit': Campojj['Nit_juridica_contratista'].value(),
                    'repre': Campojj['Nombre_representante_contratista'].value(),
                    'ccr': Campojj['Cedula_representate_contratista'].value(),
                    
                    'actiprocon': Campojj['Actividad_profesional_contratista'].value(),
                    'objsoj': Campojj['Objeto_social_contratante'].value(),
                    'finalidads': Campojj['Finalidad'].value(),
                    'servigeneral': Campojj['Servicio_manera_general'].value(),
                    'Servicon': Campojj['Servicio_prestado_contratista'].value(),
                    'contraprenum': Campojj['Contraprestacion_numeros'].value(),
                    'contraprestacion': Contraprestacion_letras,
                    'plazonum': Campojj['Plazo_sugerido_dias'].value(),
                    'plazole': Plazo_sugerido_letras,
                    'cbanc': Campojj['Banco'].value(),
                    'cuentac': Campojj['Tipo_cuenta'].value(),
                    'numcuenta': Campojj['Numero_cuenta'].value(),
                    'nomtitular': Campojj['Nombre_titular'].value(),
                    'identitular': Campojj['Cedula_titular'].value(),
                    'tipogas': Tipo_con,
                    'duranum': Campojj['Duracion_numeros'].value(),
                    'duraletras': Duracion_letras,
                    'anoomes': Anos_meses,
                    'direfc' : Campojj['Direccion_Fisica_contratante'].value(),
                    'diree' : Campojj['Correo_electronico_contratante'].value(),
                    'paragrafoc' : paragrafoc,
                    'paragraprim': pragrafo_primero,
                    }

   
    if Campojj['Paragrafo_prueba_opcional'].value() == True:
      
        variablelist['diasnum'] = Campojj['Dias_prueba_numeros'].value()
        variablelist['diasletras'] = Dias_prueba_letras
        variablelist['fech'] = Fecha_prueba

    doc_template = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS JyJ.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        print(varkey + ' ' + varval + '\n ')
        replaceTextWordDoc(varkey, varval, doc_final)

    return doc_final

def main_NyJ(Camponj):
        
    os.chdir(os.getcwd())
    
    Tipo_con = tipocon(Camponj['Tipo_con'].value())
    Anos_meses= Anosomeses(Camponj['Anos_meses'].value())
    Contraprestacion_letras = num2words(Camponj['Contraprestacion_numeros'].value(), lang='es_CO').upper()
    Plazo_sugerido_letras = num2words(Camponj['Plazo_sugerido_dias'].value(), lang='es_CO').upper()
    Duracion_letras = num2words(Camponj['Duracion_numeros'].value(), lang='es_CO').upper()
    Fecha_nacimiento_contratante_natural = formatDate(Camponj['Fecha_nacimiento_contratante_natural'].value())


    if Camponj['Paragrafo_prueba_opcional'].value() != True:
        paragrafoc = ''
    else:
        paragrafoc = """ PARAGRAFO. No obstante lo anterior, las partes iniciaron un periodo de prueba de diasletras (diasnum) DÍAS contados a partir del Fecha_prueba. Una vez cumplido este término de prueba, empezará a contar el periodo establecido del presente Contrato.
                    La finalidad de este periodo de prueba tiene como objetivo delimitar el alcance de los servicios requeridos por EL CONTRANTE y, así, lo aceptan expresamente las partes. """
        Dias_prueba_letras = num2words(Camponj['Dias_prueba_numeros'].value(), lang='es_CO').upper()
        Fecha_prueba = formatDate(Camponj['Fecha_prueba'].value())
    if Camponj['Paragrafo_primero'].value() != True:
        pragrafo_primero = ''
    else:
        pragrafo_primero = 'PARÁGRAFO PRIMERO. Las partes procederán con la realización de una “agenda de trabajo” escrito que hará parte integral del presente Contrato, con miras a cumplir y ejecutar en debida forma las obligaciones acá contenidas.'
    
    variablelist = {'razon': Camponj['Razon_social_natural'].value(),
                    'cednatu_contratante': Camponj['Cedula_contratante_natural'].value(),
                    'domicon_contratante': Camponj['Ciudad_contratante_natural'].value(),
                    'fechana_contratante': Fecha_nacimiento_contratante_natural,
                    'lugarna_contratante': Camponj['Lugar_nacimiento_contratante_natural'].value(),
                    'Razonsj_contratista': Camponj['Razon_social_juridica_contratista'].value(),
                    'Nitperj_contratista': Camponj['Nit_juridica_contratista'].value(),
                    'nombre_representante_contratista': Camponj['Nombre_representante_contratista'].value(),
                    'cedulre_contratista': Camponj['Cedula_representate_contratista'].value(),
                    'actiprocon': Camponj['Actividad_profesional_contratista'].value(),
                    'objsoj': Camponj['Objeto_social_contratante'].value(),
                    'finalidads': Camponj['Finalidad'].value(),
                    'servigeneral': Camponj['Servicio_manera_general'].value(),
                    'Servicon': Camponj['Servicio_prestado_contratista'].value(),
                    'contraprenum': Camponj['Contraprestacion_numeros'].value(),
                    'contraprestacion': Contraprestacion_letras,
                    'plazonum': Camponj['Plazo_sugerido_dias'].value(),
                    'plazole': Plazo_sugerido_letras,
                    'ccr': Camponj['Banco'].value(),
                    'cuentac': Camponj['Tipo_cuenta'].value(),
                    'numcuenta': Camponj['Numero_cuenta'].value(),
                    'nomtitular': Camponj['Nombre_titular'].value(),
                    'identitular': Camponj['Cedula_titular'].value(),
                    'tipogas': Tipo_con,
                    'duranum': Camponj['Duracion_numeros'].value(),
                    'duraletras': Duracion_letras,
                    'anoomes': Anos_meses,
                    'direfc' : Camponj['Direccion_Fisica_contratante'].value(),
                    'diree' : Camponj['Correo_electronico_contratante'].value(),
                    'paragrafoc' : paragrafoc,
                    'paragraprim': pragrafo_primero,
                    }

    if Camponj['Paragrafo_prueba_opcional'].value() == True:
        variablelist['diasnum'] = Camponj['Dias_prueba_numeros'].value()
        variablelist['diasletras'] = Dias_prueba_letras
        variablelist['fech'] = Fecha_prueba

    doc_template = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS NyJ.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        replaceTextWordDoc(varkey, varval, doc_final)

    return doc_final

def main_NyN(Camponn):
        
    os.chdir(os.getcwd())
    Tipo_con = tipocon(Camponn['Tipo_con'].value())
    Anos_meses= Anosomeses(Camponn['Anos_meses'].value())
    Contraprestacion_letras = num2words(Camponn['Contraprestacion_numeros'].value(), lang='es_CO').upper()
    Plazo_sugerido_letras = num2words(Camponn['Plazo_sugerido_dias'].value(), lang='es_CO').upper()
    Duracion_letras = num2words(Camponn['Duracion_numeros'].value(), lang='es_CO').upper()
    Fecha_nacimiento_contratante_natural = formatDate(Camponn['Fecha_nacimiento_contratante_natural'].value())
    Fecha_nacimiento_contratista = formatDate(Camponn['Fecha_nacimiento_contratista'].value(), )

    if Camponn['Paragrafo_prueba_opcional'].value() != True:
        paragrafoc = ''
    else:
        paragrafoc = """ PARAGRAFO. No obstante lo anterior, las partes iniciaron un periodo de prueba de diasletras (diasnum) DÍAS contados a partir del Fecha_prueba. Una vez cumplido este término de prueba, empezará a contar el periodo establecido del presente Contrato.
                    La finalidad de este periodo de prueba tiene como objetivo delimitar el alcance de los servicios requeridos por EL CONTRANTE y, así, lo aceptan expresamente las partes. """
        Dias_prueba_letras = num2words(Camponn['Dias_prueba_numeros'].value(), lang='es_CO').upper()
        Fecha_prueba = formatDate(Camponn['Fecha_prueba'].value())
    if Camponn['Paragrafo_primero'].value() != True:
        pragrafo_primero = ''
    else:
        pragrafo_primero = 'PARÁGRAFO PRIMERO. Las partes procederán con la realización de una “agenda de trabajo” escrito que hará parte integral del presente Contrato, con miras a cumplir y ejecutar en debida forma las obligaciones acá contenidas.'

    variablelist = {'Razonsj_natural': Camponn['Razon_social_natural'].value(),
                    'cednatu_contratante': Camponn['Cedula_contratante_natural'].value(),
                    'domicon_contratante': Camponn['Ciudad_contratante_natural'].value(),
                    'fechana_contratante': Fecha_nacimiento_contratante_natural,
                    'lugarna_contratante': Camponn['Lugar_nacimiento_contratante_natural'].value(),
                    'Nombre_natural': Camponn['Nombre_natural'].value(),
                    'cedcon': Camponn['Cedula_contratista'].value(),
                    'domicon': Camponn['Ciudad_contratista'].value(),
                    'fechana': Fecha_nacimiento_contratista,
                    'lugarna': Camponn['Lugar_nacimiento_contratista'].value(),
                    'actiprocon': Camponn['Actividad_profesional_contratista'].value(),
                    'objsoj': Camponn['Objeto_social_contratante'].value(),
                    'finalidads': Camponn['Finalidad'].value(),
                    'servigeneral': Camponn['Servicio_manera_general'].value(),
                    'Servicon': Camponn['Servicio_prestado_contratista'].value(),
                    'contraprenum': Camponn['Contraprestacion_numeros'].value(),
                    'contraprestacion': Contraprestacion_letras,
                    'plazonum': Camponn['Plazo_sugerido_dias'].value(),
                    'plazole': Plazo_sugerido_letras,
                    'ccr': Camponn['Banco'].value(),
                    'cuentac': Camponn['Tipo_cuenta'].value(),
                    'numcuenta': Camponn['Numero_cuenta'].value(),
                    'nomtitular': Camponn['Nombre_titular'].value(),
                    'identitular': Camponn['Cedula_titular'].value(),
                    'tipogas': Tipo_con,
                    'duranum': Camponn['Duracion_numeros'].value(),
                    'duraletras': Duracion_letras,
                    'anoomes': Anos_meses,
                    'direfc' : Camponn['Direccion_Fisica_contratante'].value(),
                    'diree' : Camponn['Correo_electronico_contratante'].value(),
                    'paragrafoc' : paragrafoc,
                    'paragraprim': pragrafo_primero,
                    }

    if Camponn['Paragrafo_prueba_opcional'].value() == True:
          
        variablelist['diasnum'] = Camponn['Dias_prueba_numeros'].value()
        variablelist['diasletras'] = Dias_prueba_letras
        variablelist['fech'] = Fecha_prueba 

    doc_template = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS NyN.docx"
    
    doc_final = re.sub(r'(\w)(\.docx)', r'\1_Final\2', doc_template)

    shutil.copy(doc_template, doc_final)

    for varkey, varval in variablelist.items():
        replaceTextWordDoc(varkey, varval, doc_final)

    return doc_final