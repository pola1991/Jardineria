from calendar import c
from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

# Create your models here.
"""
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name='id_producto')
    marca_producto = comuna_persona = models.CharField(max_length=30,verbose_name='marca_producto')
    descripcion_producto = models.TextField(verbose_name='descripcion_producto')
    cantidad_producto_existente = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

"""
"""
hola

hhhhhhh
class Persona(models.Model):h
    rut_persona = models.IntegerField(primary_key=True, verbose_name='rut_persona')
    dv_persona = models.IntegerField(verbose_name='dv_persona')
    nombre_completo_persona = models.CharField(max_length=50,verbose_name='nombre_completo_persona')
    direccion_persona = models.CharField(max_length=50, verbose_name='direccion_persona')
    comuna_persona = models.CharField(max_length=80,verbose_name='comuna_persona')
    Region_persona = models.CharField(max_length=80, verbose_name='region_persona')
    mail_persona = models.EmailField(verbose_name='email_persona')
    celular_persona = models.IntegerField(verbose_name='celular_persona')
    def __str__(self):
        return self.nombre_completo_persona

class Administrador(models.Model):
    id_administrador = models.IntegerField(primary_key=True, verbose_name='id_administrador')
    contrasenia_administrador = models.CharField(max_length=100, verbose_name='contrasenia') 

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True, verbose_name='id_cliente')
    contrasenia_cliente = models.CharField(max_length=100, verbose_name='contrasenia_cliente')

class Suscripcion(models.Model):
    id_suscripcion = models.IntegerField(primary_key=True, verbose_name='id_suscripcion')
    monto_donacion = models.IntegerField(verbose_name='monto_donacion')
    descuento_suscripcion = models.IntegerField(verbose_name='descuento_suscripcion') 

class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True, verbose_name='id_compra')
    fecha_compra = models.da(max_length=)
    hora_compra =
    descripcion_compra = 
    monto_total_compra =
    monto_final_compra =

class Modo_pago(models.Model):
    id_modo_pago = models.IntegerField(primary_key=True, verbose_name='id_modo_pago')
    tipo_modo_pago = models.CharField(max_length=50, verbose_name='tipo_modo_pago')
    descripcion_modo_pago = models.TextField(verbose_name='descripcion_modo_pago')


class Promocion(models.Model):
    id_promocion = models.IntegerField(primary_key=True, verbose_name='id_promocion')
    descripcion_promocion = models.TextField(verbose_name='descripcion_promocion')
    condicion_promocion =

class Descuento(models.Model):
    id_descuento = models.IntegerField(primary_key=True, verbose_name='id_descuento')
    descripcion_descuento = models.TextField(verbose_name='descripcion_descuento')
    cantidad_descuento =
    condiciones_descuento =

class Despacho(models.Model):
    id_despacho = models.IntegerField(primary_key=True, verbose_name='id_despacho')
    fecha_despacho =
    hora_despacho =
    seguimiento_despacho =

class Recepcion(models.Model):
    id_recepcion = models.IntegerField(primary_key=True, verbose_name='id_recepcion')
    fecha_recepcion =
    hora_recepcion =
"""
    