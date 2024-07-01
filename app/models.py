from django.db import models
from django.contrib.auth.models import User
from .choices import *


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    def get_email(self):
        if self.user:
            return self.user.email
        else:
            return self.email




class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def get_precio(self):
        return self.precio

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=255)
    region = models.CharField(max_length=100, choices=REGIONES_CHILE, default="REGION_BIOBIO")
    ciudad = models.CharField(max_length=100, choices=COMUNAS_POR_REGION)
    codigo_postal = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)  # 'envio' o 'facturacion'

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}, {self.estado}, {self.pais}"

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    direccion_envio = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Orden {self.id} - Cliente: {self.cliente}"

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pago(models.Model):
    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=50)
    transaccion_id = models.CharField(max_length=100)
    monto = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.transaccion_id} - Monto: {self.monto}"


