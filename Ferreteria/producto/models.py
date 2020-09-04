from django.db import models

# Create your models here.

class Producto(models.Model):
    Id = models.IntegerField(primary_key=True, editable=False)
    Stock_minimo = models.FloatField()
    Precio = models.FloatField()
    Descripcion = models.CharField(max_length=255)
    Stock = models.FloatField()
    Marca = models.CharField(max_length=100)
    Activo = models.BooleanField()
    Fecha_alta = models.DateField()
    Fecha_ultima_venta = models.DateField()
    Cantidad_vendida = models.FloatField()
    Fecha_ultimo_pedido = models.DateField()

class Usuario(models.Model):
    Id = models.IntegerField(primary_key=True, editable=False)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Empresa = models.CharField(max_length= 100)
    CUIT = models.CharField(max_length=13)
    DNI = models.IntegerField(max_length=10)
    Telefono = models.CharField(max_length=15)
    Celular = models.CharField(max_length=15)
    Mail = models.EmailField()
    Saldo = models.FloatField()
    Es_proveedor = models.BooleanField()
    Es_cliente = models.BooleanField()
    Direccion = models.CharField(max_length=255)
    Ultima_accion = models.DateField()

class Provee(models.Model):
    Id_producto = models.ManyToManyField(Producto)
    Id_usuario = models.ManyToManyField(Usuario)
    Fecha_origen = models.DateField()
    Fecha_entrega = models.DateField()
    Total = models.FloatField()
    Saldo = models.FloatField()
    Comprobante = models.FloatField()

class Compra(models.Model):
    Id_producto = models.ManyToManyField(Producto)
    Id_usuario = models.ManyToManyField(Usuario)
    Fecha_origen = models.DateField()
    Fecha_entrega = models.DateField()
    Total = models.FloatField()
    Saldo = models.FloatField()
    Comprobante = models.FloatField()