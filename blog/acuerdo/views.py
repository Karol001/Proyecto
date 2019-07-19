from django.shortcuts import render, redirect
from blog.acuerdo.forms import AcuerdoForm, AcuerdoForm_natural
from blog.acuerdo.main import main
from blog.acuerdo.main import main_natural
from blog.acuerdo.models import models
from blog.config import base_path, word_to_pdf
import os 
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.views import generic


def rnatural_view(request):
    if request.method == 'POST':
        form= AcuerdoForm_natural(request.POST)
        path = base_path + "/ACUERDO DE CONFIDENCIALIDAD Y NO COMPETENCIA_copian_Final.docx"
        PathContrato = main_natural(form)
        path = word_to_pdf(path, base_path + "/ACUERDO DE CONFIDENCIALIDAD Y NO COMPETENCIA_copian_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else: 
        form = AcuerdoForm_natural()
    return render(request,'acuerdo_confidencialidad/acuerdo_form.html',{'form':form})


def representante_view(request):
    if request.method == 'POST':
        form= AcuerdoForm(request.POST)
        path = base_path + "/ACUERDO DE CONFIDENCIALIDAD Y NO COMPETENCIA_copia_Final.docx"
        PathContrato = main(form)
        path = word_to_pdf(path, base_path + "/ACUERDO DE CONFIDENCIALIDAD Y NO COMPETENCIA_copia_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path): 
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else: 
        form = AcuerdoForm()
    return render(request,'acuerdo_confidencialidad/acuerdo_form.html',{'form':form})
