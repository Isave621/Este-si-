"""guiapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from principal.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
    path('formulario/', formulario),
    path('contactar/', contactar),
    path('indexprincipal/', indexprincipal),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', inicio, name="sesion"),
    path('accounts/profile/admin/', admin.site.urls),
    path('accounts/profile/salir/', salir),
    path('accounts/profile/contacto/', formulario),
    path('contacto/', formulario),
    path('accounts/profile/paquete/', tour),
    path('paquete/', tour),
    path('accounts/profile/sobre/', nosotres),
    path('sobre/', nosotres),
    path('registro/', RegistroUsuario.as_view(),),
    path('accounts/profile/registro/', RegistroUsuario.as_view(),),
    path('accounts/profile/hotel/', Hoteles),
    path('hotel/', Hoteles),
    path('accounts/profile/restaurante/', Restaurantes),
    path('restaurante/', Restaurantes),
    path('accounts/profile/servicio/', Servicios),
    path('servicio/', Servicios),
    path('perfil/crear', nuevo_perfil),
    path('perfil/', posts,),


    path('comentarios/', ListadoComentarios.as_view(template_name = "comentarios/inicio.html"), name='2leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un comentarios o registro 
    path('comentarios/detalle/<int:pk>', ComentariosDetalle.as_view(template_name = "comentarios/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo comentarios o registro  
    path('comentarios/crear', ComentariosCrear.as_view(template_name = "comentarios/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un comentarioso registro de la Base de Datos 
    path('comentarios/editar/<int:pk>', ComentariosActualizar.as_view(template_name = "comentarios/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un comentarios o registro de la Base de Datos 
    path('comentarios/eliminar/<int:pk>', ComentariosEliminar.as_view(), name='comentarios/eliminar.html'),       
   
    path('empresa/', ListadoEmpresa.as_view(template_name = "empresa/inicio.html"), name='5leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un empresa o registro 
    path('empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "empresa/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo empresa o registro  
    path('empresa/crear', EmpresaCrear.as_view(template_name = "empresa/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un empresao registro de la Base de Datos 
    path('empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "empresa/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un empresa o registro de la Base de Datos 
    path('empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='empresa/eliminar.html'),

    path('persona/', ListadoPersona.as_view(template_name = "persona/inicio.html"), name='13leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un persona o registro 
    path('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "persona/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo persona o registro  
    path('persona/crear', PersonaCrear.as_view(template_name = "persona/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un personao registro de la Base de Datos 
    path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "persona/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un persona o registro de la Base de Datos 
    path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='persona/eliminar.html'),  


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)