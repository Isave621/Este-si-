
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from ast import Delete
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser







class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comentarios(models.Model):
    idcomentarios = models.IntegerField(db_column='idComentarios', primary_key=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comentarios'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    idempresa = models.IntegerField(db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.IntegerField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sitioweb = models.CharField(db_column='SitioWeb', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombrecontacto = models.CharField(db_column='NombreContacto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerocontacto = models.CharField(db_column='NumeroContacto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nit = models.IntegerField(db_column='Nit', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'


class Estadocliente(models.Model):
    idestadocliente = models.IntegerField(db_column='idEstadoCliente', primary_key=True)  # Field name made lowercase.
    activo = models.CharField(db_column='Activo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    inactivo = models.CharField(db_column='Inactivo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estadocliente'


class Eventos(models.Model):
    ideventos = models.IntegerField(db_column='idEventos', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerocontacto = models.IntegerField(db_column='NumeroContacto', blank=True, null=True)  # Field name made lowercase.
    horarioinicio = models.CharField(db_column='HorarioInicio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horariofinal = models.CharField(db_column='HorarioFinal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sitioweb = models.CharField(db_column='SitioWeb', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    tipoeventos_idtipoeventos = models.IntegerField(db_column='TipoEventos_idTipoEventos')  # Field name made lowercase.
    reservas_idreservas = models.IntegerField(db_column='Reservas_idReservas')  # Field name made lowercase.
    reservas_restaurantes_idrestaurante = models.IntegerField(db_column='Reservas_Restaurantes_idRestaurante')  # Field name made lowercase.
    reservas_restaurantes_tipolugar_idtipolugar = models.IntegerField(db_column='Reservas_Restaurantes_Tipolugar_idtipolugar')  # Field name made lowercase.
    ofertas_idofertas = models.IntegerField(db_column='Ofertas_idOfertas')  # Field name made lowercase.
    serviciotour_idserviciotour = models.IntegerField(db_column='ServicioTour_idServicioTour')  # Field name made lowercase.
    comentarios_idcomentarios = models.IntegerField(db_column='Comentarios_idComentarios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventos'


class Lugar(models.Model):
    idsitiosturisticos = models.IntegerField(db_column='idSitiosTuristicos', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    empresa_idempresa = models.IntegerField(db_column='Empresa_idEmpresa')  # Field name made lowercase.
    tipolugar_idtipolugar = models.IntegerField(db_column='Tipolugar_idtipolugar')  # Field name made lowercase.
    eventos_ideventos = models.IntegerField(db_column='Eventos_idEventos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lugar'


class Ofertas(models.Model):
    idofertas = models.IntegerField(db_column='idOfertas', primary_key=True)  # Field name made lowercase.
    precios = models.CharField(db_column='Precios', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.IntegerField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.IntegerField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ofertas'

        
class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField(null = True, blank = True)
    #imagen = models.ImageField(null = True, blank = True)}
    imagen = models.ImageField(upload_to="imagenes" , null=True)

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=200)
    comentario = models.TextField(null = True, blank = True)
    imagen = models.ImageField(upload_to="imagenes" , null=True)


class Usuario(models.Model):
    nombre = models.CharField(max_length=200, null = True)
    correo = models.CharField(max_length=200, null = True)
    celular = models.CharField(max_length=200, null = True) 
    descripcion = models.TextField(null = True, blank = True)
    imagen = models.ImageField(upload_to="imagenes" , null=True)

class Persona(models.Model):
    field_idcliente = models.IntegerField(db_column=' idCliente', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    identificacion = models.IntegerField(db_column='Identificacion', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    celular = models.IntegerField(db_column='Celular', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contraseña', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipopersona_idtipocliente = models.IntegerField(db_column='TipoPersona_idTipoCliente')  # Field name made lowercase.
    empresa_idempresa = models.IntegerField(db_column='Empresa_idEmpresa')  # Field name made lowercase.
    tipodocumento_idtipodocumento = models.IntegerField(db_column='TipoDocumento_idTipoDocumento')  # Field name made lowercase.
    estadocliente_idestadocliente = models.IntegerField(db_column='EstadoCliente_idEstadoCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Reservas(models.Model):
    idreservas = models.IntegerField(db_column='idReservas', primary_key=True)  # Field name made lowercase.
    estador = models.CharField(db_column='EstadoR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='Cliente', max_length=45, blank=True, null=True)  # Field name made lowercase.
    comprobante = models.CharField(db_column='Comprobante', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cupoadulto = models.IntegerField(db_column='CupoAdulto', blank=True, null=True)  # Field name made lowercase.
    cuponino = models.IntegerField(db_column='CupoNiño', blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    tiporeserva_idtiporeserva = models.IntegerField(db_column='TipoReserva_idTipoReserva')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservas'


class Rutas(models.Model):
    idrutas = models.IntegerField(db_column='idRutas', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rutas'


class Serviciotour(models.Model):
    idserviciotour = models.IntegerField(db_column='idServicioTour', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    rutas_idrutas = models.IntegerField(db_column='Rutas_idRutas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serviciotour'


class Tipodocumento(models.Model):
    idtipodocumento = models.IntegerField(db_column='idTipoDocumento', primary_key=True)  # Field name made lowercase.
    denominacion = models.CharField(db_column='Denominacion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipodocumento'


class Tipoeventos(models.Model):
    idtipoeventos = models.IntegerField(db_column='idTipoEventos', primary_key=True)  # Field name made lowercase.
    denominacion = models.CharField(db_column='Denominacion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipoeventos'


class Tipolugar(models.Model):
    idtipolugar = models.IntegerField(primary_key=True)
    denominacion = models.CharField(db_column='Denominacion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipolugar'


class Tiporeserva(models.Model):
    idtiporeserva = models.IntegerField(db_column='idTipoReserva', primary_key=True)  # Field name made lowercase.
    precio = models.CharField(db_column='Precio', max_length=45, blank=True, null=True)  # Field name made lowercase.
    actividades = models.CharField(db_column='Actividades', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiporeserva'
