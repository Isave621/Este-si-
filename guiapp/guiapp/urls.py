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
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', UsuarioFormulario, name="sesion"),
    path('accounts/profile/admin/', admin.site.urls),
    path('accounts/profile/salir/', salir),
    path('accounts/profile/contacto/', contactar),
    path('contacto/', contactar),
    path('accounts/profile/paquete/', tour),
    path('paquete/', tour),
    path('accounts/profile/sobre/', nosotres),
    path('sobre/', nosotres),
    path('registro/', RegistroUsuario.as_view(),name="registro"),
    path('accounts/profile/registro/', RegistroUsuario.as_view(),),
    path('accounts/profile/restaurante/', posts),
    path('restaurante/', posts),
    path('accounts/profile/servicio/', posts),
    path('servicio/', posts),
    path('hotel/', posts,),  
    path('salir/', salir, name="salir"),
    path('reportes/', generar_reporte.as_view(), name="generar_reporte"),
    path('hotel/comentarios/', formularioPerfil)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)