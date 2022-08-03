from http.client import HTTPResponse
from tkinter import Variable
from urllib import request
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

from .utils import render_to_pdf
from .forms import RegistroForm
from django.views.generic import View



# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


# Create your views here.


# Inicio de sesion

@login_required  

def salir(request):
    logout(request)
    return redirect('/')

# Fin de inicio de sesion



# Subir imagenes de los servicios

def posts(request):
    posts = Perfil.objects.all().order_by('imagen', 'nombre', 'direccion')
    return render(request, 'hotel.html', {"posts": posts})

# Fin de imagenes de los servicios



# Formulario comentarios

def formularioPerfil(request):
    usuario = PerfilUsuario.objects.all().order_by('imagen', 'nombre', 'comentario')
    variables = {"usuario" : usuario}

    if request.POST: 
        persona = PerfilUsuario()   
        persona.nombre = request.POST.get('txtNombre')
        persona.comentario = request.POST.get('txtComentario')
        persona.imagen = request.FILES.get('txtImagen')

        try: 
            persona.save()
            variables['mensaje'] = 'Guardado'
        except: 
            variables['mensaje'] ='No se guardo'
    
    return render (request, 'perfil/comentario.html', variables)
    
# Fin de formulario comentarios



# Vista 'principal'
def inicio(request):
    return render(request,'index.html')

# Vista de 'contacto'
def contacto(request):
    return render(request, 'contact.html')

#Vista de 'tour'
def tour(request):
    return render(request, 'package.html')

#Vista 'sobre nosotros'
def nosotres(request):
    return render(request, 'about.html')



# Registro de ususario

class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registro.html"
    form_class = RegistroForm
    
    def get_success_url(self):        
        return reverse('sesion')

# Fin de registro de ususario



# Formulario contacto

def contactar(request):
    if request.method == "POST":
        asunto = request.POST ["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["isavelasco1206@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
    return render (request, "formularioContacto.html")

# Fin de formulario contacto



# Reportes

class generar_reporte(View):
    def get(self,request):
        template_name="reporte.html"
        hotel=Perfil.objects.all()
        data = {
            'count':hotel.count(),
            'hotel':hotel   
        }
        pdf=render_to_pdf(template_name,data)
        return HttpResponse(pdf,content_type='application/pdf')

# Fin de reportes



#Formulario de perfil de usuario

def UsuarioFormulario(request):
    persona = Usuario.objects.all().order_by('nombre', 'correo', 'celular', 'descripcion', 'imagen')
    variables = {"persona" : persona}

    if request.POST: 
        perfil= Usuario()   
        perfil.nombre = request.POST.get('txtNombre')
        perfil.correo = request.POST.get('txtCorreo')
        perfil.celular = request.POST.get('txtCelular')
        perfil.descripcion = request.POST.get('txtDescripcion')
        perfil.imagen = request.FILES.get('txtImagen')

        try: 
            perfil.save()
            variables['mensaje'] = 'Guardado'
        except: 
            variables['mensaje'] ='No se guardo'
    
    return render (request, 'perfil/editar.html', variables)
    