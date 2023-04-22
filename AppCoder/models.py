from django.db import models

class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    dni = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Articulo(models.Model):
    producto = models.TextField(max_length=100)
    marca = models.TextField(max_length=100, default="samsung")
    cantidad = models.TextField(max_length=100, default="1")
 
    def __str__(self):
        return f"{self.producto} - {self.marca} - {self.cantidad}"


class Envio(models.Model):
    direccion = models.TextField(max_length=100)
    ciudad = models.TextField(max_length=100, default=" ")
    provincia = models.TextField(max_length=100, default=" ")
    cp = models.TextField(max_length=100, default=" ")
    def __str__(self):
        return f"{self.direccion} - {self.ciudad} - {self.provincia} - {self.cp}"