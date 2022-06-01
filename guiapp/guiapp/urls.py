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
from django.contrib import admin
from django.urls import path, include
from principal.views import *

urlpatterns = [
    path('', inicio),
    path('admin/', admin.site.urls),
    path('formulario/', formulario),
    path('contactar/', contactar),
    path('indexprincipal/', indexprincipal),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', inicio),
    path('accounts/profile/salir/', salir),
    path('registro/', registroUsuario, name="registroUsuario"),


    path('tiporeserva/', ListadoTiporeserva.as_view(template_name = "tiporeserva/inicio.html"), name='1leer'),
    
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tiporeserva o registro 
    path('tiporeserva/detalle/<int:pk>', TiporeservaDetalle.as_view(template_name = "tiporeserva/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tiporeserva o registro  
    path('tiporeserva/crear', TiporeservaCrear.as_view(template_name = "tiporeserva/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tiporeservao registro de la Base de Datos 
    path('tiporeserva/editar/<int:pk>', TiporeservaActualizar.as_view(template_name = "tiporeserva/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tiporeserva o registro de la Base de Datos 
    path('tiporeserva/eliminar/<int:pk>', TiporeservaEliminar.as_view(), name='tiporeserva/eliminar.html'), 


    path('comentarios/', ListadoComentarios.as_view(template_name = "comentarios/inicio.html"), name='2leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un comentarios o registro 
    path('comentarios/detalle/<int:pk>', ComentariosDetalle.as_view(template_name = "comentarios/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo comentarios o registro  
    path('comentarios/crear', ComentariosCrear.as_view(template_name = "comentarios/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un comentarioso registro de la Base de Datos 
    path('comentarios/editar/<int:pk>', ComentariosActualizar.as_view(template_name = "comentarios/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un comentarios o registro de la Base de Datos 
    path('comentarios/eliminar/<int:pk>', ComentariosEliminar.as_view(), name='comentarios/eliminar.html'),    



    path('rutas/', ListadoRutas.as_view(template_name = "rutas/inicio.html"), name='3leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un rutas o registro 
    path('rutas/detalle/<int:pk>', RutasDetalle.as_view(template_name = "rutas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo rutas o registro  
    path('rutas/crear', RutasCrear.as_view(template_name = "rutas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un rutaso registro de la Base de Datos 
    path('rutas/editar/<int:pk>', RutasActualizar.as_view(template_name = "rutas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un rutas o registro de la Base de Datos 
    path('rutas/eliminar/<int:pk>', RutasEliminar.as_view(), name='rutas/eliminar.html'),    


    path('tipolugar/', ListadoTipolugar.as_view(template_name = "tipolugar/inicio.html"), name='4leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipolugar o registro 
    path('tipolugar/detalle/<int:pk>', TipolugarDetalle.as_view(template_name = "tipolugar/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo tipolugar o registro  
    path('tipolugar/crear', TipolugarCrear.as_view(template_name = "tipolugar/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un tipolugaro registro de la Base de Datos 
    path('tipolugar/editar/<int:pk>', TipolugarActualizar.as_view(template_name = "tipolugar/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un tipolugar o registro de la Base de Datos 
    path('tipolugar/eliminar/<int:pk>', TipolugarEliminar.as_view(), name='tipolugar/eliminar.html'),    
    
    

    path('empresa/', ListadoEmpresa.as_view(template_name = "empresa/inicio.html"), name='5leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un empresa o registro 
    path('empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "empresa/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo empresa o registro  
    path('empresa/crear', EmpresaCrear.as_view(template_name = "empresa/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un empresao registro de la Base de Datos 
    path('empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "empresa/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un empresa o registro de la Base de Datos 
    path('empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='empresa/eliminar.html'),
    





    path('estadocliente/', ListadoEstadocliente.as_view(template_name = "estadocliente/inicio.html"), name='6leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Estadocliente o registro 
    path('estadocliente/detalle/<int:pk>', EstadoclienteDetalle.as_view(template_name = "estadocliente/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Estadocliente o registro  
    path('estadocliente/crear', EstadoclienteCrear.as_view(template_name = "estadocliente/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Estadoclienteo registro de la Base de Datos 
    path('estadocliente/editar/<int:pk>', EstadoclienteActualizar.as_view(template_name = "estadocliente/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Estadocliente o registro de la Base de Datos 
    path('estadocliente/eliminar/<int:pk>', EstadoclienteEliminar.as_view(), name='estadocliente/eliminar.html'),    

    
    
    
    path('tipodocumento/', ListadoTipodocumento.as_view(template_name = "tipodocumento/inicio.html"), name='7leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipodocumento o registro 
    path('tipodocumento/detalle/<int:pk>', TipodocumentoDetalle.as_view(template_name = "tipodocumento/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo tipodocumento o registro  
    path('tipodocumento/crear', TipodocumentoCrear.as_view(template_name = "tipodocumento/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un tipodocumentoo registro de la Base de Datos 
    path('tipodocumento/editar/<int:pk>', TipodocumentoActualizar.as_view(template_name = "tipodocumento/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un tipodocumento o registro de la Base de Datos 
    path('tipodocumento/eliminar/<int:pk>', TipodocumentoEliminar.as_view(), name='tipodocumento/eliminar.html'),   
  




    path('reservas/', ListadoReservas.as_view(template_name = "reservas/inicio.html"), name='8leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un reservas o registro 
    path('reservas/detalle/<int:pk>', ReservasDetalle.as_view(template_name = "reservas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo reservas o registro  
    path('reservas/crear', ReservasCrear.as_view(template_name = "reservas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un reservaso registro de la Base de Datos 
    path('reservas/editar/<int:pk>', ReservasActualizar.as_view(template_name = "reservas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un reservas o registro de la Base de Datos 
    path('reservas/eliminar/<int:pk>', ReservasEliminar.as_view(), name='reservas/eliminar.html'),    
   

 

    path('serviciotour/', ListadoServiciotour.as_view(template_name = "serviciotour/inicio.html"), name='9leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Serviciotour o registro 
    path('serviciotour/detalle/<int:pk>', ServiciotourDetalle.as_view(template_name = "serviciotour/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Serviciotour o registro  
    path('serviciotour/crear', ServiciotourCrear.as_view(template_name = "serviciotour/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Serviciotouro registro de la Base de Datos 
    path('serviciotour/editar/<int:pk>', ServiciotourActualizar.as_view(template_name = "serviciotour/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Serviciotour o registro de la Base de Datos 
    path('serviciotour/eliminar/<int:pk>', ServiciotourEliminar.as_view(), name='serviciotour/eliminar.html'),




    path('ofertas/', ListadoOfertas.as_view(template_name = "ofertas/inicio.html"), name='10leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Ofertas o registro 
    path('ofertas/detalle/<int:pk>', OfertasDetalle.as_view(template_name = "ofertas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Ofertas o registro  
    path('ofertas/crear', OfertasCrear.as_view(template_name = "ofertas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Ofertaso registro de la Base de Datos 
    path('ofertas/editar/<int:pk>', OfertasActualizar.as_view(template_name = "ofertas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Ofertas o registro de la Base de Datos 
    path('ofertas/eliminar/<int:pk>', OfertasEliminar.as_view(), name='ofertas/eliminar.html'),    


    path('lugar/', ListadoLugar.as_view(template_name = "lugar/inicio.html"), name='11leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un lugar o registro 
    path('lugar/detalle/<int:pk>', LugarDetalle.as_view(template_name = "lugar/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo lugar o registro  
    path('lugar/crear', LugarCrear.as_view(template_name = "lugar/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un lugaro registro de la Base de Datos 
    path('lugar/editar/<int:pk>', LugarActualizar.as_view(template_name = "lugar/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un lugar o registro de la Base de Datos 
    path('lugar/eliminar/<int:pk>', LugarEliminar.as_view(), name='lugar/eliminar.html'),  




    path('eventos/', ListadoEventos.as_view(template_name = "eventos/inicio.html"), name='12leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Eventos o registro 
    path('eventos/detalle/<int:pk>', EventosDetalle.as_view(template_name = "eventos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Eventos o registro  
    path('eventos/crear', EventosCrear.as_view(template_name = "eventos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Eventoso registro de la Base de Datos 
    path('eventos/editar/<int:pk>', EventosActualizar.as_view(template_name = "eventos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Eventos o registro de la Base de Datos 
    path('eventos/eliminar/<int:pk>', EventosEliminar.as_view(), name='eventos/eliminar.html'),  


    path('persona/', ListadoPersona.as_view(template_name = "persona/inicio.html"), name='13leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un persona o registro 
    path('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "persona/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo persona o registro  
    path('persona/crear', PersonaCrear.as_view(template_name = "persona/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un personao registro de la Base de Datos 
    path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "persona/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un persona o registro de la Base de Datos 
    path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='persona/eliminar.html'),  


    path('tipoeventos/', ListadoTipoeventos.as_view(template_name = "tipoeventos/inicio.html"), name='14leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un tipoeventos o registro 
    path('tipoeventos/detalle/<int:pk>', TipoeventosDetalle.as_view(template_name = "tipoeventos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo tipoeventos o registro  
    path('tipoeventos/crear', TipoeventosCrear.as_view(template_name = "tipoeventos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un tipoeventoso registro de la Base de Datos 
    path('tipoeventos/editar/<int:pk>', TipoeventosActualizar.as_view(template_name = "tipoeventos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un tipoeventos o registro de la Base de Datos 
    path('tipoeventos/eliminar/<int:pk>', TipoeventosEliminar.as_view(), name='tipoeventos/eliminar.html'),    

]


    

    

   



    
