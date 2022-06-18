from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, PerfilForm



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

@login_required  


#def posts(request):
    #posts=Perfil.objects.all()
    #try:
       # objeto_especifico = Perfil.objects.get(nombre=1) # Cambiar por el parametro deseado, pk, codename unico, etc
    #except Perfil.DoesNotExist:
    #    objeto_especifico = None
   # return render(request, "perfil/inicio.html", {"posts": posts, 'objeto_especifico': objeto_especifico})

def posts(request):
    posts = Perfil.objects.all().order_by('imagen')
    return render(request, 'perfil/inicio.html', {"posts": posts})

def nuevo_perfil(request): 
    form = PerfilForm()
    

    if request.method == 'post':
        form = PerfilForm(request.post, request.FILES)

        if form.is_valid():
           post = form.save()
           return redirect("post:posts")

    else:
        form = PerfilForm()

    return render(request, 'perfil/crear.html', {"form":form})

    

class HotelDetalle (DetailView):
    model = Perfil

        
        






def inicio(request):
    return render(request,'index.html')

def salir(request):
    logout(request)
    return redirect('/')

def contacto(request):
    return render(request, 'contact.html')

def tour(request):
    return render(request, 'package.html')

def nosotres(request):
    return render(request, 'about.html')


class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registro.html"
    form_class = RegistroForm
    
    def get_success_url(self):        
        return reverse('sesion')

def Hoteles(request):
    return render(request, 'hotel.html')

def Restaurantes(request):
    return render(request, 'restaurante.html')

def Servicios(request):
    return render(request, 'servicio.html')







def formulario(request):
    return render (request, "formularioContacto.html")

def indexprincipal(request):
    return render (request, "index.html")



def contactar(request):
    if request.method == "POST":
        asunto = request.POST ["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["jhornym8@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render (request, "contactoExitoso.html")
    return render (request, "formulario.html")





#
class ListadoComentarios(ListView):
    model = Comentarios
    
    
class ComentariosCrear(SuccessMessageMixin, CreateView):
    model =Comentarios
    form = Comentarios
    fields = "__all__"
    success_message ='Comentarios creada correctamente'
     
    def get_success_url(self):        
        return reverse('2leer') # Redireccionamos a la vista principal 'leer'

class ComentariosDetalle (DetailView):
    model =Comentarios

class  ComentariosActualizar(SuccessMessageMixin,UpdateView):
    model =  Comentarios
    form = Comentarios
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Comentarios Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('2leer') # Redireccionamos a la vista principal 'leer'
class ComentariosEliminar(SuccessMessageMixin, DeleteView): 
    model = Comentarios 
    form = Comentarios
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Comentarios Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('2leer') # Redireccionamos a la vista principal 'leer'




# 

class ListadoEmpresa(ListView):
    model = Empresa
    
    
class EmpresaCrear(SuccessMessageMixin, CreateView):
    model =Empresa
    form = Empresa
    fields = "__all__"
    success_message ='Empresa creada correctamente'
     
    def get_success_url(self):        
        return reverse('5leer') # Redireccionamos a la vista principal 'leer'

class EmpresaDetalle (DetailView):
    model =Empresa

class  EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =  Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Empresa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('5leer') # Redireccionamos a la vista principal 'leer'
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa 
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Empresa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('5leer') # Redireccionamos a la vista principal 'leer'



#
class ListadoPersona(ListView):
    model = Persona
    
    
class PersonaCrear(SuccessMessageMixin, CreateView):
    model =Persona
    form = Persona
    fields = "__all__"
    success_message ='Persona creada correctamente'
     
    def get_success_url(self):        
        return reverse('13leer') # Redireccionamos a la vista principal 'leer'

class PersonaDetalle (DetailView):
    model =Persona

class  PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('13leer') # Redireccionamos a la vista principal 'leer'
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona 
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('13leer') # Redireccionamos a la vista principal 'leer'

