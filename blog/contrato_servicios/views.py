from django.shortcuts import render, redirect
from blog.contrato_servicios.forms import ServicioForm1, ServicioForm2, ServicioForm3, ServicioForm4
from blog.contrato_servicios.main import main_JyN, main_JyJ, main_NyJ, main_NyN
import os 
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.views import generic
from blog.config import base_path, word_to_pdf


def Jyn_view(request):
    if request.method == 'POST':
        form= ServicioForm1(request.POST)
        path = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS JyN_Final.docx"
        PathContrato = main_JyN(form)
        path = word_to_pdf(path, base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS JyN_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else: 
        form = ServicioForm1()
    return render(request,'contrato_servicios/contrato_form.html',{'form':form})

def JyJ_view(request):
    if request.method == 'POST':
        form2= ServicioForm2(request.POST)
        path = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS JyJ_Final.docx"
        PathContrato = main_JyJ(form2)
        path = word_to_pdf(path, base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS JyJ_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path): 
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else: 
        form2= ServicioForm2()
    return render(request,'contrato_servicios/contrato_form2.html',{'form2':form2})

def NyJ_view(request):
    if request.method == 'POST':
        form3= ServicioForm3(request.POST)
        path = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS NyJ_Final.docx"
        PathContrato = main_NyJ(form3)
        path = word_to_pdf(path, base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS NyJ_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path): 
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else: 
        form3= ServicioForm3()
    return render(request,'contrato_servicios/contrato_form3.html',{'form3':form3})

def NyN_view(request):
    if request.method == 'POST':
        form4= ServicioForm4(request.POST)
        path = base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS NyN_Final.docx"
        PathContrato = main_NyN(form4)
        path = word_to_pdf(path, base_path + "/CONTRATO DE PRESTACIÓN DE SERVICIOS NyN_Final.pdf")
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        print(os.path.exists(file_path))
        if os.path.exists(file_path): 
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                response['Content-Type'] = 'application/vnd.ms-word; charset=utf-16'
                return response
        raise Http404("Parent node was not found.")
    else: 
        form4= ServicioForm4()
    return render(request,'contrato_servicios/contrato_form4.html',{'form4':form4})





