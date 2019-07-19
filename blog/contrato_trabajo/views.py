from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from blog.config import base_path, word_to_pdf
from blog.contrato_trabajo.forms import ContratoJuridicoForm, ContratoNaturalForm
from blog.contrato_trabajo.main import main_juridica, main_natural

import os

def home(request):
  
    return render(request, 'blog/home.html')

def contrato_juridico_view(request):
    if request.method == "POST":
        path = base_path + "/CONTRATO DE TRABAJO A TÉRMINO INDEFINIDO JURIDICA_Final.docx"
        form = ContratoJuridicoForm(request.POST)
        pathContrato = main_juridica(form)
        path = word_to_pdf(path, base_path + "/CONTRATO DE TRABAJO A TÉRMINO INDEFINIDO JURIDICA_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else:
        form = ContratoJuridicoForm()
    return render(request, 'contrato_trabajo/form_contrato.html', {'form': form})

def contrato_natural_view(request):
    if request.method == "POST":
        path = base_path + "/CONTRATO DE TRABAJO A TÉRMINO INDEFINIDO NATURAL_Final.docx"
        form = ContratoNaturalForm(request.POST)
        pathContrato = main_natural(form)
        path = word_to_pdf(path, base_path + "/CONTRATO DE TRABAJO A TÉRMINO INDEFINIDO NATURAL_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else:
        form = ContratoNaturalForm()
    return render(request, 'contrato_trabajo/form_contrato.html', {'form': form})
    

